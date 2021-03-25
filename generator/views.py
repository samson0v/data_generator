from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import TemplateView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Schema, Column, DataSet
from .forms import SchemaForm, ColumnFormSet
from .tasks import generate_data


class SchemaListView(LoginRequiredMixin, TemplateView):
    """
    Return Schema models list
    """

    model = Schema
    template_name = 'generator/schema_list.html'

    def get(self, request, *args, **kwargs):
        output = {
            'object_list': Schema.objects.filter(user__exact=request.user).order_by('-id')
        }
        return self.render_to_response(output)


def schema_create_view(request):
    if request.method == 'GET':
        formset = ColumnFormSet(request.GET or None)
        form = SchemaForm(request.GET or None)
    elif request.method == 'POST':
        formset = ColumnFormSet(request.POST)
        form = SchemaForm(request.POST)

        if form.is_valid() and formset.is_valid():
            schema_name = form.cleaned_data.get('name')
            schema = Schema(name=schema_name, user=request.user)
            schema.save()

            for form in formset:
                column_name = form.cleaned_data.get('name')
                column_type = form.cleaned_data.get('type')
                column_start_from = form.cleaned_data.get('start_from')
                column_to = form.cleaned_data.get('to')
                column_order = form.cleaned_data.get('order')

                column = Column(name=column_name, type=column_type, start_from=column_start_from, to=column_to,
                                schema=schema, order=column_order)
                column.save()
        else:
            return render(request, 'generator/create_schema.html', {'columns': formset, 'form': form})

        return redirect('generator:schema-list')

    return render(request, 'generator/create_schema.html', {'columns': formset, 'form': form})


def schema_update_view(request, pk):
    schema = Schema.objects.filter(pk=pk).first()
    if request.method == 'GET':
        formset = ColumnFormSet(request.GET or None, instance=schema)
        form = SchemaForm(request.GET or None, instance=schema)

    elif request.method == 'POST':
        formset = ColumnFormSet(request.POST, instance=schema)
        form = SchemaForm(request.POST, instance=schema)

        if form.is_valid() and formset.is_valid():
            schema_name = form.cleaned_data.get('name')
            schema = Schema.objects.filter(pk=pk).first()
            schema.name = schema_name
            schema.modified = timezone.now()
            schema.save()

            formset.save()
        else:
            return render(request, 'generator/create_schema.html', {'columns': formset, 'form': form})

        return redirect('generator:schema-list')

    return render(request, 'generator/create_schema.html', {'columns': formset, 'form': form})


class SchemaDeleteView(LoginRequiredMixin, DeleteView):
    model = Schema
    success_url = reverse_lazy('generator:schema-list')
    template_name = 'generator/delete_schema.html'


class CreateDataSet(LoginRequiredMixin, CreateView):
    """
    Creating DataSet model using celery task generate_data()
    """

    model = DataSet
    template_name = 'generator/create_dataset.html'
    fields = '__all__'

    def get(self, request, *args, **kwargs):
        schema = Schema.objects.filter(pk__exact=self.kwargs['pk']).first()

        return self.render_to_response(
            {'object_list': DataSet.objects.filter(
                schema__exact=schema).order_by('-id')})

    def post(self, request, *args, **kwargs):
        schema = Schema.objects.filter(pk__exact=self.kwargs['pk']).first()
        rows_num = int(request.POST.get('rows'))

        data_set = DataSet.objects.create(schema=schema)

        generate_data.delay(rows_num, [column_id.pk for column_id in schema.column_set.all()], data_set.id)
        return redirect('generator:create-dataset', pk=schema.pk)

from django import forms
from django.forms.models import inlineformset_factory

from .models import Column, Schema


class SchemaForm(forms.ModelForm):
    """
    Form for creating Schema model with custom field
    """

    name = forms.CharField(label='',  max_length=254, widget=forms.TextInput(attrs={
        'class': 'input',
        'placeholder': 'Schema name'
    }))

    class Meta:
        model = Schema
        fields = ['name']
        exclude = ()


class ColumnForm(forms.ModelForm):
    """
    Form for creating Column model with custom fields
    """

    name = forms.CharField(label='',  max_length=254, widget=forms.TextInput(attrs={
        'class': 'input',
        'placeholder': 'Column name'
    }))
    start_from = forms.IntegerField(label='', required=False, widget=forms.NumberInput(attrs={
        'class': 'input',
        'placeholder': 'From',
    }))
    to = forms.IntegerField(label='', required=False, widget=forms.NumberInput(attrs={
        'class': 'input',
        'placeholder': 'To'
    }))
    order = forms.IntegerField(label='', widget=forms.NumberInput(attrs={
        'class': 'input',
        'placeholder': 'Order',
        'min': '1'
    }))

    class Meta:
        model = Column
        fields = ['name', 'type',  'start_from', 'to', 'order']
        exclude = ()


ColumnFormSet = inlineformset_factory(Schema, Column, form=ColumnForm, extra=1)


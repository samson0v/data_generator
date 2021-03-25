from django.contrib import admin

from .models import Column, Schema, DataSet


class ColumnInline(admin.StackedInline):
    model = Column
    extra = 1


class SchemaAdmin(admin.ModelAdmin):
    fieldsets = []
    inlines = [ColumnInline]


admin.site.register(Schema, SchemaAdmin)
admin.site.register(DataSet)

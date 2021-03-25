from django.urls import path

from . import views


app_name = 'generator'

urlpatterns = [
    path('schema-list/', views.SchemaListView.as_view(), name='schema-list'),
    path('schema-list/<int:pk>/create-dataset/', views.CreateDataSet.as_view(), name='create-dataset'),
    path('create-schema/', views.schema_create_view, name='schema-create'),
    path('delete-schema/<int:pk>/', views.SchemaDeleteView.as_view(), name='schema-delete'),
    path('update-schema/<int:pk>/', views.schema_update_view, name='schema-update')
]

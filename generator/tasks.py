from celery import shared_task
from django.core.files import File

from generator.services.export_data import generate_csv
from generator.models import DataSet, Column


@shared_task
def generate_data(rows_num, columns_id, data_set_id):
    """
    Editing DataSet model, init file and updating status
    Parameters
    ----------
    rows_num : int
    columns_id : list
    data_set_id : list
    """
    generate_csv(rows_num, [Column.objects.filter(pk__exact=item).first() for item in columns_id])
    data_set = DataSet.objects.filter(pk__exact=data_set_id).first()
    data_set.file.save('data_set.csv', File(open('data_set.csv')))
    data_set.status = DataSet.Status.READY
    data_set.save()

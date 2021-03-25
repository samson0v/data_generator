from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.db import models


class Schema(models.Model):
    """
    Schema model

    Attributes
    ----------
    name : str
    created : DateTime
        field that added automatically
    modified : DateTime
        field that added when model update orr retrieve
    user: ForeignKey
    """
    name = models.CharField(max_length=254)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Column(models.Model):
    """
    Column model

    Attributes
    ----------
    name : str
    type : SelectField
    order : int
    start_from : int
    to : int
    schema : ForeignKey
    """
    class Type(models.TextChoices):
        TEXT = 'TEXT', _('Text')
        FULL_NAME = 'FULL_NAME', _('Full Name')
        JOB = 'JOB', _('Job')
        EMAIL = 'EMAIL', _('Email')
        DOMAIN_NAME = 'DOMAIN_NAME', _('Domain Name')
        PHONE_NUMBER = 'PHONE_NUMBER', _('Phone Number')
        COMPANY_NAME = 'COMPANY_NAME', _('Company Name')
        INTEGER = 'INTEGER', _('Integer')
        ADDRESS = 'ADDRESS', _('Address')
        DATE = 'DATE', _('Date')

    name = models.CharField(max_length=254)
    type = models.CharField(max_length=12, choices=Type.choices)
    order = models.PositiveIntegerField()
    start_from = models.IntegerField(null=True, blank=True)
    to = models.IntegerField(null=True, blank=True)
    schema = models.ForeignKey('Schema', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class DataSet(models.Model):
    """
    DataSet model

    Attributes
    ----------
    created : DateTime
    status : ChoiceField
    file : FileField
    schame : ForeignKey
    """
    class Status(models.TextChoices):
        PROCESSING = 'PROCESSING', _('Processing')
        READY = 'READY', _('Ready')

    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=Status.choices, max_length=10,  default=Status.PROCESSING)
    file = models.FileField(upload_to='data_sets/', null=True, blank=True)
    schema = models.ForeignKey('Schema', on_delete=models.CASCADE)

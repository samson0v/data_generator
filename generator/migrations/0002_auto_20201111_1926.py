# Generated by Django 3.1.3 on 2020-11-11 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='column',
            name='start_from',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='column',
            name='to',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

# Generated by Django 3.2.12 on 2022-08-16 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campus', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trashbin',
            name='amount',
            field=models.FloatField(default=0),
        ),
    ]

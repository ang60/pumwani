# Generated by Django 4.2.2 on 2023-06-22 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0043_obstetric_historyformfive_obstetric_historyformfour_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='obstetric_historyformone',
            name='GRAVID',
            field=models.BooleanField(choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=3),
        ),
    ]
# Generated by Django 4.2.2 on 2023-06-21 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0037_alter_obstetric_history_signature'),
    ]

    operations = [
        migrations.AddField(
            model_name='obstetric_history',
            name='obstetric_date',
            field=models.DateField(null=True),
        ),
    ]

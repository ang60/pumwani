# Generated by Django 4.2.2 on 2023-06-21 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0035_alter_obstetric_history_edd_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='obstetric_history',
            name='date_of_quickening',
            field=models.DateField(max_length=10, null=True),
        ),
    ]

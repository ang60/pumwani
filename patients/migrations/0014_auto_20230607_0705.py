# Generated by Django 2.2.12 on 2023-06-07 07:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0013_auto_20230606_1454'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='anaesthic_record',
            new_name='anaesthetic_record',
        ),
    ]
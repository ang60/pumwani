# Generated by Django 4.2.2 on 2023-06-19 07:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0021_alter_payment_patient'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='patient',
        ),
    ]
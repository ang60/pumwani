# Generated by Django 4.2.2 on 2023-06-19 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0025_payment_other_payment_alter_payment_payment_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='other_payment',
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_type',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
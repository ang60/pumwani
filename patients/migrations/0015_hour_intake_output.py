# Generated by Django 2.2.12 on 2023-06-12 08:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0014_auto_20230607_0705'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hour', models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='output',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vomit', models.CharField(max_length=100, null=True)),
                ('stool', models.CharField(max_length=100, null=True)),
                ('Alimentary_amount', models.CharField(max_length=100, null=True)),
                ('others', models.CharField(max_length=100, null=True)),
                ('urine_specificgraity', models.CharField(max_length=100, null=True)),
                ('N_gast', models.CharField(max_length=100, null=True)),
                ('hour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.Hour')),
            ],
        ),
        migrations.CreateModel(
            name='intake',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bottle', models.CharField(max_length=100, null=True)),
                ('infused', models.CharField(max_length=100, null=True)),
                ('intravenous_type', models.CharField(max_length=100, null=True)),
                ('amount', models.IntegerField(null=True)),
                ('alimentary_type', models.CharField(max_length=100, null=True)),
                ('hour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.Hour')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.Patient')),
            ],
        ),
    ]

# Generated by Django 4.2.2 on 2023-06-22 09:22

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import jsignature.fields
import patients.models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0042_alter_obstetric_history_gravid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Obstetric_historyformfive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condition', models.CharField(max_length=100, null=True)),
                ('twin', models.BooleanField(null=True)),
                ('TB', models.BooleanField(null=True)),
                ('essen_hypert', models.BooleanField(null=True)),
                ('sample', models.CharField(max_length=100, null=True)),
                ('heart_did', models.BooleanField(null=True)),
                ('relation', models.CharField(max_length=100, null=True)),
                ('history_date', models.DateField(null=True)),
                ('smoking', models.BooleanField(null=True)),
                ('alcohol', models.BooleanField(null=True)),
                ('sports', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Obstetric_historyformfour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('illness', models.BooleanField(null=True)),
                ('obstetric_date', models.DateField(null=True)),
                ('treatment', models.CharField(max_length=50, null=True)),
                ('others', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Obstetric_historyformone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LMP', models.DateField(null=True, validators=[patients.models.lmpdate_validator])),
                ('EDD', models.DateField(null=True, validators=[patients.models.edddate_validator])),
                ('GRAVID', models.BooleanField(choices=[('yes', 'Yes'), ('no', 'No')], default=False)),
                ('PARITY', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)])),
            ],
        ),
        migrations.CreateModel(
            name='Obstetric_historyformsix',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blood_group', models.CharField(max_length=5, null=True)),
                ('rhesus', models.CharField(max_length=10, null=True)),
                ('hb', models.FloatField(null=True)),
                ('rbs', models.FloatField(null=True)),
                ('vdrl', models.BooleanField(default=False)),
                ('serology', models.CharField(max_length=100, null=True)),
                ('hep_b', models.BooleanField(default=False)),
                ('urinalysis', models.CharField(max_length=100, null=True)),
                ('clinics_attended', models.TextField(blank=True)),
                ('number_of_visits', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Obstetric_historyformthree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('life_state', models.BooleanField(null=True)),
                ('menarche', models.IntegerField(null=True)),
                ('cycle', models.CharField(max_length=20, null=True)),
                ('length_menstrual', models.CharField(max_length=20, null=True)),
                ('regularity', models.CharField(max_length=20, null=True)),
                ('flow', models.CharField(max_length=20, null=True)),
                ('present_pregnancy', models.CharField(max_length=20, null=True)),
                ('date_of_quickening', models.DateField(null=True)),
                ('gestation_on_firstvisit', models.IntegerField(null=True)),
                ('clinical_estimation', models.CharField(max_length=100, null=True)),
                ('complaints', models.CharField(max_length=100, null=True)),
                ('length_pregnancy', models.CharField(max_length=20, null=True)),
                ('Complaints', models.CharField(max_length=30, null=True)),
                ('pain', models.CharField(max_length=30, null=True)),
                ('bleeding', models.BooleanField(null=True)),
                ('vomiting', models.BooleanField(null=True)),
                ('frequency', models.IntegerField(null=True)),
                ('operations', models.IntegerField(null=True)),
                ('blood_transfusion', models.BooleanField(null=True)),
                ('recent_drugs_taken', models.CharField(max_length=30, null=True)),
                ('admitting_officer', models.CharField(max_length=30, null=True)),
                ('signature', jsignature.fields.JSignatureField(null=True)),
                ('time', models.TimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Obstetric_historyformtwo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.IntegerField(null=True)),
                ('sex', models.CharField(max_length=10, null=True)),
                ('place_of_birth', models.CharField(max_length=30, null=True)),
                ('weight', models.IntegerField(null=True)),
                ('length_labour', models.CharField(max_length=10, null=True)),
                ('Mode_of_delivery', models.CharField(max_length=30, null=True)),
                ('pueperium', models.IntegerField(null=True)),
                ('complications', models.CharField(max_length=30, null=True)),
                ('feeding', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='antenatal_records',
            name='family_history',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.obstetric_historyformone'),
        ),
        migrations.DeleteModel(
            name='Obstetric_history',
        ),
    ]

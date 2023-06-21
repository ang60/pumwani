# Generated by Django 4.2.2 on 2023-06-21 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0038_obstetric_history_obstetric_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='anaesthetic_record',
            old_name='date',
            new_name='record_date',
        ),
        migrations.RenameField(
            model_name='antenatal_records',
            old_name='date_records',
            new_name='antenatal_date_records',
        ),
        migrations.RenameField(
            model_name='magnesium_sulphate',
            old_name='date',
            new_name='Magnesium_sulphate_date',
        ),
        migrations.RenameField(
            model_name='obstetric_history',
            old_name='date',
            new_name='history_date',
        ),
        migrations.RenameField(
            model_name='past_medical_and_surgical_history',
            old_name='date',
            new_name='medical_date',
        ),
        migrations.RenameField(
            model_name='pre_anaesthetic',
            old_name='date',
            new_name='Pre_anaesthetic_date',
        ),
        migrations.RenameField(
            model_name='pre_operationone',
            old_name='date',
            new_name='Pre_operationone_date',
        ),
        migrations.RenameField(
            model_name='report_labourone',
            old_name='date',
            new_name='duration_date',
        ),
        migrations.RenameField(
            model_name='vital_chart',
            old_name='date',
            new_name='vital_date',
        ),
        migrations.AlterField(
            model_name='obstetric_history',
            name='date_of_quickening',
            field=models.DateField(null=True),
        ),
    ]

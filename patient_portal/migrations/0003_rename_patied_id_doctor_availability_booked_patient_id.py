# Generated by Django 3.2.5 on 2022-03-20 23:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient_portal', '0002_doctor_availability_booked'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor_availability_booked',
            old_name='patied_id',
            new_name='patient_id',
        ),
    ]
# Generated by Django 4.1.5 on 2023-01-15 01:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_assestment_gender'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assestment',
            old_name='job_description',
            new_name='job_title',
        ),
    ]
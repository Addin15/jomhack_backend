# Generated by Django 4.1.5 on 2023-01-15 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_provider_email_alter_provider_phone_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assestment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.TextField()),
                ('age', models.IntegerField()),
                ('job_description', models.TextField()),
                ('existing_condition', models.TextField()),
                ('family_history', models.TextField()),
                ('smoker', models.BooleanField()),
                ('married', models.BooleanField()),
            ],
        ),
    ]

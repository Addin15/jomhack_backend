# Generated by Django 4.1.5 on 2023-01-14 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('about', models.TextField()),
                ('category', models.CharField(max_length=100)),
                ('keys', models.JSONField()),
                ('link', models.URLField()),
            ],
        ),
        migrations.AddField(
            model_name='provider',
            name='email',
            field=models.EmailField(default=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='provider',
            name='phone',
            field=models.CharField(default=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='provider',
            name='website',
            field=models.URLField(default=True, null=True),
        ),
    ]
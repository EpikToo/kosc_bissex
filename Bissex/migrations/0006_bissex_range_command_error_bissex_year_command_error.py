# Generated by Django 4.1.2 on 2022-12-23 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bissex', '0005_bissex_range_bissex_year_delete_bissex'),
    ]

    operations = [
        migrations.AddField(
            model_name='bissex_range',
            name='command_error',
            field=models.CharField(blank=True, default='OK', max_length=100),
        ),
        migrations.AddField(
            model_name='bissex_year',
            name='command_error',
            field=models.CharField(blank=True, default='OK', max_length=100),
        ),
    ]

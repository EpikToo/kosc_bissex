# Generated by Django 4.1.2 on 2022-12-23 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Bissex', '0006_bissex_range_command_error_bissex_year_command_error'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Bissex_year',
            new_name='model_Bissex_annee',
        ),
        migrations.RenameModel(
            old_name='Bissex_range',
            new_name='model_Bissex_range',
        ),
    ]

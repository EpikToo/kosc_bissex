# Generated by Django 4.1.2 on 2022-12-19 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bissex', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bissex_history',
            options={'ordering': ['command_date']},
        ),
        migrations.AddField(
            model_name='bissex_history',
            name='command_date',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='bissex_history',
            name='command_entry',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='bissex_history',
            name='command_result',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='bissex_history',
            name='command_type',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]

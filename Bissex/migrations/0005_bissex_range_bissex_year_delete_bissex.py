# Generated by Django 4.1.2 on 2022-12-23 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bissex', '0004_alter_bissex_command_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bissex_range',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('command_type', models.CharField(default='Bissex_range', max_length=100)),
                ('command_entry', models.CharField(blank=True, default='', max_length=100)),
                ('command_result', models.CharField(blank=True, default='', max_length=100)),
                ('command_date', models.DateTimeField(auto_now_add=True, max_length=100)),
            ],
            options={
                'ordering': ['command_date'],
            },
        ),
        migrations.CreateModel(
            name='Bissex_year',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('command_type', models.CharField(default='Bissex_year', max_length=100)),
                ('command_entry', models.CharField(blank=True, default='', max_length=100)),
                ('command_result', models.BooleanField(blank=True, default='Null', max_length=100, null=True)),
                ('command_date', models.DateTimeField(auto_now_add=True, max_length=100)),
            ],
            options={
                'ordering': ['command_date'],
            },
        ),
        migrations.DeleteModel(
            name='Bissex',
        ),
    ]

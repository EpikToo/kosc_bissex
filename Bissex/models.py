from django.db import models

class model_Bissex_annee(models.Model):
    command_type = models.CharField(max_length=100, default='Bissex_year')
    command_entry = models.CharField(max_length=100, blank=True, default='')
    command_result = models.BooleanField(max_length=100, blank=True, null=True, default='Null')
    command_date = models.DateTimeField(max_length=100, auto_now_add=True)
    command_error = models.CharField(max_length=100, blank=True, default='OK')
    class Meta:
        ordering = ['command_date']

class model_Bissex_range(models.Model):
    command_type = models.CharField(max_length=100, default='Bissex_range')
    command_entry = models.CharField(max_length=100, blank=True, default='')
    command_result = models.CharField(max_length=100, blank=True, default='')
    command_date = models.DateTimeField(max_length=100, auto_now_add=True)
    command_error = models.CharField(max_length=100, blank=True, default='OK')
    class Meta:
        ordering = ['command_date']
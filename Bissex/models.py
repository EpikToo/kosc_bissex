from django.db import models

class Bissex_history(models.Model):
    command_type = models.CharField(max_length=100, blank=True, default='')
    command_entry = models.CharField(max_length=100, blank=True, default='')
    command_result = models.CharField(max_length=100, blank=True, default='')
    command_date = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        ordering = ['command_date']
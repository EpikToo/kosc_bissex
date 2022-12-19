from django.db import models

class Bissex_history(models.Model):
    command_type = models.CharField
    command_entry = models.CharField
    command_result = models.CharField
    command_date = models.DateTimeField

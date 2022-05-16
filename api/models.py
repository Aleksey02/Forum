from django.db import models

# Create your models here.
class Checkbox(models.Model):
    name = models.CharField(max_length=150)
    is_checked = models.BooleanField(default=False)

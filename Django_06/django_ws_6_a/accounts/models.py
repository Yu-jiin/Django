from django.db import models

# Create your models here.
class Account(models.Model):
    work = models.CharField(max_length=100)
    content = models.TextField()
    is_complted = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
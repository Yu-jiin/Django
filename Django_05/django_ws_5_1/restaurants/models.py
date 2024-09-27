from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    address = models.TextField()
    phone_number = models.TextField()
    

# Restaurant.objects.create(name='HELLs KITCHEN', description='고든램지의
#  식당', address='라스베가스', phone_number='000-00-000')
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


installation_type_choice = ('FW', 'PC', 'FWPC')

class Client(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=40)
    installation = models.CharField(max_length=100)
    installation_type = models.CharField(max_length=4, default='')
    installation_date = models.TextField(max_length=10, default='')
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=9)
    location_longitude = models.FloatField(default=0)
    location_latitude = models.FloatField(default=0)


    def __str__(self) -> str:
        return self.full_name
    
class SuperuserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    permission = models.IntegerField(default=0)

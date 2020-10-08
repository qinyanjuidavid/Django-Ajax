from django.db import models
from django.contrib.auth.models import User




class Task(models.Model):
    title=models.CharField(max_length=200)
    date=models.DateTimeField(auto_now_add=True)
    completed=models.BooleanField(default=False)


    def __str__(self):
        return str(self.title)
class MyUser(models.Model):
    userid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50,blank=False,null=False,verbose_name="Name")
    phone_number=models.CharField(max_length=15,blank=False,null=False,verbose_name="Phone")
    email=models.EmailField(max_length=50,blank=False,null=False,verbose_name="Email")


    def __str__(self):
        return str(self.name)

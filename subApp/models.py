from django.db import models

# Create your models here.
class hiring(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=250)
    email=models.CharField(max_length=100)
    dob=models.CharField(max_length=50)
    telphone=models.CharField(max_length=20)
    Add=models.CharField(max_length=100)
    totalExp=models.IntegerField()
    position=models.CharField(max_length=50)
    portfolio=models.FileField(upload_to='resume/',max_length=300)
    def __str__(self):
        return self.name +"-"+ self.position 
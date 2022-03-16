from django.db import models

# Create your models here.
class Contactdetails(models.Model):
    trustMail = models.CharField(max_length=100)
    trustAddress = models.CharField(max_length=300)
    trustOrg = models.CharField(max_length=100)
    trustPhonenumber = models.CharField(max_length=100)
    trustFrontimage = models.ImageField(upload_to='frontImage')

class Whatwedo(models.Model):
    name = models.CharField(max_length=100)
    content = models.CharField(max_length=100)
    image = models.ImageField(upload_to='frontImage')

class Addimage(models.Model):
    projectid = models.IntegerField()
    date=models.CharField(max_length=100)
    image = models.ImageField(upload_to='frontImage')

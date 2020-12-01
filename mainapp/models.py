from django.db import models
from django.contrib import admin
# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Csv(models.Model):
    csv = models.FileField(upload_to='projects')
    csv_tag = models.CharField(max_length=50)
    csv_flag = models.CharField(max_length=50)
    
    def __str__(self):
        return str(self.csv_flag)

from django.db import models

# Create your models here.

class Group(models.Model):
    name = models.CharField('Dashboard Group', max_length=20)

class Dashboard(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    url = models.CharField('Source URL', max_length=200)

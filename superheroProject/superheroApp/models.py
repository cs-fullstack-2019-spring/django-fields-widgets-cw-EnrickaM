from django.db import models

# Create your models here.

class superheroApplication(models.Model):
    name=models.CharField(max_length=200,default='')
    city_or_Orgin=models.CharField(max_length=200,default='')
    areyourichordoyouhavesuperpowers=models.CharField(max_length=10,default='')
    # dropbox=models.CharField(max_length=200)
    ifyouhavesuperpowerwhichones=models.CharField(max_length=200,default='')
    whichofthefollowingareyou=models.CharField(max_length=200)
    # checkbox = models.CharField(max_length=200)
    give_us_3_examples_when_you_used_your_super_ablities=models.CharField(max_length=200)



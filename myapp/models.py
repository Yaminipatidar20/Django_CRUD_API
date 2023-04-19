from django.db import models

class ElectricDevice(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField()
    description=models.TextField()
    
    def __str__(self):
        return self.name
    

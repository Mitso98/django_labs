from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=60)
    
    def __str__(self) -> str:
        return self.name
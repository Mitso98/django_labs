from django.db import models
# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=50)
    born_at = models.DateField(null=True)
    died_at = models.DateField(null=True)
    contact = models.CharField(null=True, max_length=100)
    # books = models.CharField(null=True, max_length=50)
    bio = models.CharField(null=True, max_length=200)

    def __str__(self):
        return self.name

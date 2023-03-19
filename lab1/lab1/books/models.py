from django.db import models
from authors.models import Author
# Create your models here.


class Book(models.Model):
    published_at = models.DateField(null=True, blank=True)
    summary = models.CharField(null=True, max_length=200, blank=True)
    country = models.CharField(null=True, max_length=50, blank=True)
    link = models.URLField(null=True, blank=True)
    writer = models.ForeignKey(Author, default=None, on_delete=models.CASCADE)
    name = models.CharField(default=None, max_length=50, blank=True)

    def __str__(self):
        return self.name


from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0)])
    publication_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title
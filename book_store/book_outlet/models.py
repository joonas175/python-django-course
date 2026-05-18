
from django.db import models
from django.core.validators import MinValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.DecimalField(
        max_digits=6, decimal_places=2, validators=[MinValueValidator(0)])
    publication_date = models.DateField(null=True, blank=True)
    slug = models.SlugField(default="", null=False, db_index=True, blank=True, editable=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("book-detail", kwargs={"book_slug": self.slug})


# To create and save:
# harry_potter = Book(title="Harry Potter 1", author="JK Rowling", price=19.99)
# harry_potter.save()

# One liner:
# Book.objects.create(title="Harry Potter 2", author="JK Rowling", price=29.99)


# To delete:
# harry_potter = Book.objects.get(id=1)
# harry_potter.delete()

# To filter:
# Book.objects.filter(author="JK Rowling")
# Book.objects.filter(price__gt=20)
# Book.objects.filter(price__lt=20)
# Book.objects.filter(title__contains="Harry")

# https://docs.djangoproject.com/en/6.0/ref/models/querysets/#field-lookups


# OR clause
# from django.db.models import Q
# Book.objects.filter(Q(author="JK Rowling") | Q(price__gt=20))

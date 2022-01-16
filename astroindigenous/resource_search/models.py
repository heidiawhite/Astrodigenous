from datetime import date
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import gettext_lazy as _


INDIGENOUS_AUTHOR_CHOICES = (
    (None, "Unknown"),
    (False, "No"),
    (True, "Yes")
)

def less_than_current_year(value):
    if value > date.today().year:
        raise ValidationError(
            _('%(requested_year) is in the future!'),
            params={'requested_year': value}
        )

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class Format(models.Model):
    name = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return self.name


class Resource(models.Model):
    author = models.CharField(max_length=128)
    title = models.CharField(max_length=128)
    links = models.TextField()
    rec_type = models.CharField(max_length=128)
    summary = models.TextField(blank = True)
    indigenous_author = models.BooleanField(choices = INDIGENOUS_AUTHOR_CHOICES, null = True) 
    year = models.IntegerField(blank=True, validators=[
        less_than_current_year, MinValueValidator(1970), MaxValueValidator(9999)
    ])
    tags = models.ManyToManyField(Tag)
    formats = models.ManyToManyField(Format)
    languages = models.ManyToManyField(Language)

    def __str__(self):
        return f"{self.id}: {self.title}"

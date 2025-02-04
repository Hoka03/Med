from django.db import models
from django.core.validators import MinValueValidator
from datetime import datetime

from apps.sponsors.validations import phone_validate


class University(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)

    def __str__(self):
        return self.name


class Student(models.Model):
    class LevelChoices(models.IntegerChoices):
        MAGISTRAL = 1, "Magistral"
        Bachelor = 2, 'Bachelor'

    university = models.ForeignKey(University, on_delete=models.PROTECT, null=True)
    full_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=13, validators=[phone_validate])
    level = models.PositiveSmallIntegerField(choices=LevelChoices.choices)
    contract = models.DecimalField(max_digits=20, decimal_places=0, validators=[MinValueValidator(1)])
    sponsored_amount = models.DecimalField(max_digits=20, decimal_places=0, default=0)
    year = models.PositiveIntegerField(default=datetime.now().year)

    def __str__(self):
        return self.full_name
from django.db import models
from django.core.validators import ValidationError
from datetime import datetime

from apps.sponsors.validations import phone_validate


class University(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Student(models.Model):
    class LevelChoices(models.IntegerChoices):
        MAGISTRATURA = 1, 'Magistratura'
        BAKALAVR = 2, 'Bakalavr'

    university = models.ForeignKey(University, on_delete=models.PROTECT, null=True)
    full_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=13, validators=[phone_validate])
    level = models.PositiveSmallIntegerField(choices=LevelChoices.choices)
    contract = models.DecimalField(max_digits=20, decimal_places=1)
    sponsored_amount = models.DecimalField(max_digits=20, decimal_places=1)
    year = models.PositiveIntegerField(default=datetime.now().year)

    def clean(self):
        super().clean()

        if not self.university:
            raise ValidationError('University must be entered.')

        if self.sponsored_amount > self.contract:
            raise ValidationError('Sponsored amount cannot exceed the contract amount')

    def __str__(self):
        return self.full_name
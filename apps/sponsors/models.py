from django.db import models
from django.core.validators import MinValueValidator, ValidationError

from apps.sponsors.validations import phone_validate
from apps.students.models import Student


class Sponsor(models.Model):
    class TypeChoices(models.IntegerChoices):
        LEGAL_ENTITY = 1, 'Legal Entity'
        PHYSICAL_PERSON = 2, 'Physical Person'

    class StatusChoices(models.IntegerChoices):
        ALL = 1, 'All'
        NEW = 2, 'New'
        MODERATION = 3, 'Moderation'
        CONFIRMED = 4, 'Confirmed'
        CANCELED = 5, 'Canceled'

    class PaymentChoices(models.IntegerChoices):
        CLICK = 1, 'Click'
        PAYME = 2, 'Payme'
        UZCARD = 3, 'Uzcard'

    full_name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=13, validators=[phone_validate])
    amount = models.DecimalField(max_digits=15, decimal_places=1)
    company_name = models.CharField(max_length=250, blank=True, null=True)
    type_choice = models.PositiveSmallIntegerField(choices=TypeChoices.choices)
    status = models.PositiveSmallIntegerField(choices=StatusChoices.choices)
    payment_type = models.PositiveSmallIntegerField(choices=PaymentChoices.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    spent_amount = models.DecimalField(max_digits=15, decimal_places=1, validators=[MinValueValidator(0)])

    def clean(self):
        super().clean()
        if self.spent_amount > self.amount:
            raise ValidationError('Spent amount cannot exceed the total amount.')

        if self.type_choice == self.TypeChoices.LEGAL_ENTITY and not self.company_name:
            raise ValidationError('Company name is required for Legal Entities.')

        if self.type_choice == self.TypeChoices.PHYSICAL_PERSON and self.company_name:
            raise ValidationError('Company name should not be provided for Physical Persons.')

    def spend_money(self, amount):
        if amount > self.amount:
            raise ValidationError('Cannot spend more than the available amount.')
        self.amount -= amount
        self.spent_amount += amount
        self.save()

    def __str__(self):
        return f"{self.full_name} ({self.get_type_choice_display()})"


class SponsorStudent(models.Model):
    sponsor = models.ForeignKey(Sponsor, on_delete=models.PROTECT)
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=15, decimal_places=1, validators=[MinValueValidator(0)])

    def __str__(self):
        return f"{self.sponsor} sponsors {self.student}"

from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import SponsorStudent


@receiver(post_save, sender=SponsorStudent)
def update_sponsor_amount(instance, **kwargs):
    sponsor = instance.sponsor
    sponsor.spend_money(instance.amount)
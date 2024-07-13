from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save

from apps.sponsors.models import SponsorStudent, Sponsor
from apps.students.models import Student


@receiver(post_save, sender=SponsorStudent)
def post_save_sponsor_student(instance, created, *args, **kwargs):
    if not created:
        return instance

    sponsor = instance.sponsor
    student = instance.student
    amount = instance.amount

    student.sponsored_amount += amount
    student.save()

    sponsor.spent_amount += amount
    sponsor.save()

    return instance


@receiver(pre_save, sender=SponsorStudent)
def update_sponsor_spent_amount(instance, *args, **kwargs):
    old_obj = SponsorStudent.objects.filter(pk=instance.pk).first()
    if not old_obj:
        return instance
    extra = old_obj.amount - instance.amount

    old_obj.student.sponsored_amount = old_obj.student.sponsored_amount - extra
    old_obj.student.save()

    old_obj.sponsor.spent_amount = old_obj.sponsor.spent_amount - extra
    old_obj.sponsor.save()
    return instance


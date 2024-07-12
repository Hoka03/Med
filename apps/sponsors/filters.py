import django_filters

from .models import Sponsor


class SponsorFilter(django_filters.FilterSet):
    class Meta:
        model = Sponsor
        fields = ['type_choice', 'status', 'payment_type',]

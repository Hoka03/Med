from django import forms
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib import messages
from django_filters.views import FilterView

from apps.sponsors.models import Sponsor
from apps.sponsors.filters import SponsorFilter


class IndexTemplateView(TemplateView):
    template_name = 'index.html'


class SponsorCreateView(CreateView):
    class SponsorForm(forms.ModelForm):
        class Meta:
            model = Sponsor
            fields = '__all__'
            exclude = ('spent_amount', 'status')

    model = Sponsor
    template_name = 'sponsors/sponsor.html'
    form_class = SponsorForm
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sponsors"] = Sponsor.objects.all()
        self.filterset = SponsorFilter(self.request.GET, queryset=context['sponsors'])
        context['sponsors'] = self.filterset.qs
        context['filter'] = self.filterset
        return context

    def post(self, request, *args, **kwargs):
        data = request.POST
        form = self.SponsorForm(data=data)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully created.')
        else:
            messages.error(request, 'There were errors in your form')
        return redirect('sponsor')


class SponsorUpdateView(UpdateView):
    model = Sponsor
    fields = ['full_name', 'phone_number', 'amount', 'company_name', 'type_choice', 'status', 'payment_type',
              'spent_amount']
    template_name = 'sponsors/sponsor-edit.html'
    success_url = reverse_lazy('sponsor')


class SponsorDeleteView(DeleteView):
    model = Sponsor
    template_name = 'sponsors/sponsor-delete.html'
    success_url = reverse_lazy('sponsor')


class SponsorDetailView(DetailView):
    model = Sponsor
    template_name = 'sponsors/sponsor-detail.html'
    context_object_name = 'sponsors'


class SponsorListView(FilterView):
    model = Sponsor
    context_object_name = 'sponsors'
    template_name = 'sponsors/sponsor_list.html'
    filterset_class = SponsorFilter
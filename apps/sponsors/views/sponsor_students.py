from django import forms
from django.core.validators import ValidationError
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib import messages

from apps.sponsors.models import SponsorStudent


class SponsorStudentCreateView(CreateView):
    class SponsorStudentForm(forms.ModelForm):
        class Meta:
            model = SponsorStudent
            fields = '__all__'

    model = SponsorStudent
    template_name = 'sponsor_students/sponsor_student.html'
    extra_context = {
        'sponsor_students': SponsorStudent.objects.all()
    }
    form_class = SponsorStudentForm
    success_url = reverse_lazy('sponsor_student')


class SponsorStudentUpdateView(UpdateView):
    model = SponsorStudent
    fields = ['sponsor', 'student', 'amount']
    template_name = 'sponsor_students/sponsor-student-edit.html'
    success_url = reverse_lazy('sponsor_student')

    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except ValidationError as e:
            messages.error(self.request, e.message)
            return self.form_invalid(form)


class SponsorStudentDeleteView(DeleteView):
    model = SponsorStudent
    template_name = 'sponsor_students/sponsor-student-delete.html'
    success_url = reverse_lazy('sponsor')


class SponsorStudentDetail(DetailView):
    model = SponsorStudent
    template_name = 'sponsor_students/sponsor-student-detail.html'
    context_object_name = 'sponsor_students'

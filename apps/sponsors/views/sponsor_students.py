from django import forms
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy


from apps.sponsors.models import Sponsor, SponsorStudent


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
    model = Sponsor
    fields = ['sponsor', 'student', 'amount']
    template_name = 'sponsor_students/sponsor_student-edit.html'
    success_url = reverse_lazy('sponsor')


class SponsorStudentDeleteView(DeleteView):
    model = Sponsor
    template_name = 'sponsor_students/sponsor_student_delete.html'
    success_url = reverse_lazy('sponsor')


class SponsorStudentDetail(DetailView):
    model = SponsorStudent
    template_name = 'sponsor_students/sponsor_student_detail.html'
    context_object_name = 'sponsor_students'

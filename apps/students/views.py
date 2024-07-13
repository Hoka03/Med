from django import forms
from django.shortcuts import redirect
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.contrib import messages
from django.urls import reverse_lazy

from apps.students.models import Student


class StudentCreateView(CreateView):
    class StudentForm(forms.ModelForm):
        class Meta:
            model = Student
            fields = '__all__'
            exclude = ('sponsored_amount',)

    model = Student
    extra_context = {
        "students": Student.objects.all(),
    }
    template_name = 'students/student.html'
    form_class = StudentForm
    ordering = ['-year']

    def post(self, request, *args, **kwargs):
        data = request.POST
        form = self.StudentForm(data=data)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student Created.')
        else:
            messages.error(request, form.errors)
        return redirect('student')


class StudentUpdateView(UpdateView):
    model = Student
    fields = ['university', 'full_name', 'phone_number', 'level', 'contract', 'sponsored_amount']
    template_name = 'students/student-edit.html'
    success_url = reverse_lazy('student')


class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'students/student-delete.html'
    success_url = reverse_lazy('student')


class StudentDetailView(DetailView):
    model = Student
    template_name = 'students/student-detail.html'
    context_object_name = 'students'



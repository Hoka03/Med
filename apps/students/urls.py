from django.urls import path
from . import views


urlpatterns = [
    path('students/', views.StudentCreateView.as_view(), name='student'),
    path('student-edit/<int:pk>/', views.StudentUpdateView.as_view(), name='student_edit'),
    path('student-delete/<int:pk>/', views.StudentDeleteView.as_view(), name='student_delete'),
    path('student-detail/<int:pk>/', views.StudentDetailView.as_view(), name='student_detail'),
]
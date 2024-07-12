from django.urls import path
from apps.sponsors.views import sponsors, sponsor_students


urlpatterns = [
    # ================================= Sponsors ==============================================
    path('', sponsors.IndexTemplateView.as_view(), name='home'),
    path('sponsors/', sponsors.SponsorCreateView.as_view(), name='sponsor'),
    path('sponsor-edit/<int:pk>/', sponsors.SponsorUpdateView.as_view(), name='sponsor_edit'),
    path('sponsor-delete/<int:pk>/', sponsors.SponsorDeleteView.as_view(), name='sponsor_delete'),
    path('sponsor-detail/<int:pk>/', sponsors.SponsorDetailView.as_view(), name='sponsor_detail'),
    path('sponsor-filter/', sponsors.SponsorListView.as_view(), name='sponsor_filter'),
    # =====================================   Sponsor Student ===================================
    path('sponsor-students/', sponsor_students.SponsorStudentCreateView.as_view(),
         name='sponsor_student'),
    path('sponsor-students-update/<int:pk>/', sponsor_students.SponsorStudentUpdateView.as_view(),
         name='sponsor_student_edit'),
    path('sponsor-students-delete/<int:pk>/', sponsor_students.SponsorStudentDeleteView.as_view(),
         name='sponsor_student_delete'),
    path('sponsor-students-detail/<int:pk>/', sponsor_students.SponsorStudentDetail.as_view(),
         name='sponsor_student_detail'),
]
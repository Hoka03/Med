
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    path('', include('apps.sponsors.urls')),
    path('students/', include('apps.students.urls')),
]

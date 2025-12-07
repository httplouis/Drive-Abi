from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Include admin URLs once
    path('', include('myapp.urls')),  # Include app-specific URLs
]
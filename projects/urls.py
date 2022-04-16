from django.urls import path 
from .import views
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    path("", views.project_index, name='project_index'),
    path("<int:pk>/", views.project_detail, name='project_detail'), 
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
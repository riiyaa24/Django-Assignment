from django.contrib import admin
from django.urls import path
from images import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload/', views.image_upload, name='image_upload'),
]

from django.urls import path
from django.contrib import admin
from .views import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
]

# apps/home/urls.py
from django.urls import path
from django.http import HttpResponse

urlpatterns = [
    path('', lambda request: HttpResponse("🎉 Django App is working on AWS EC2")),
]

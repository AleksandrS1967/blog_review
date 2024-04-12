from django.urls import path

from main.views import contact, index

urlpatterns = [
    path('', index),
    path('contact', contact)
]

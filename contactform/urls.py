from django.urls import path

from contactform import views

urlpatterns=[
    path('contact/',views.contact,name='contact'),
]
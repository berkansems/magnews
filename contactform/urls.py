from django.urls import path

from contactform import views

urlpatterns=[
    path('contactadd/',views.contact_add,name='contact_add')
]
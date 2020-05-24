from django.urls import path

from main import views

urlpatterns=[
    path('',views.home, name = 'home'),
    path('about/',views.about,name='about'),
    path('category/',views.category,name='category'),
    path('news/',views.news,name='news'),
    path('panel/',views.panel,name='panel'),
]
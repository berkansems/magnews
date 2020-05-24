from django.urls import path

from news import views

urlpatterns =[
    path('news/<str:pk>/',views.news_detail,name='news_detail'),
    path('newslist/',views.news_list,name='news_list'),
]
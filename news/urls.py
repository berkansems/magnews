from django.urls import path

from news import views

urlpatterns =[
    path('news/<str:pk>/',views.news_detail,name='news_detail'),
    path('list/',views.news_list,name='news_list'),
    path('add/',views.add_news,name='add_news'),
    path('error/',views.error,name='error'),
    path('delete/<str:pk>/',views.delete,name='deleteNews'),
    path('news_edit/<str:pk>/',views.news_edit,name='news_edit'),
]
from django.urls import path

from book import views

urlpatterns =[
    path('addbook/', views.add_book, name='add_book'),
    path('updatebook/', views.update_book, name='update_book'),
    path('booklist/', views.book_list, name='book_list'),
    path('deletebook/<str:pk>/', views.delete_book, name='delete_book'),

]
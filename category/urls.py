from django.urls import path
from . import views
urlpatterns=[
    path('catlist/',views.cat_list,name='cat_list'),
    path('catadd/',views.cat_add,name='cat_add'),
    path('catdelete/<str:pk>/',views.cat_delete,name='cat_delete'),
]
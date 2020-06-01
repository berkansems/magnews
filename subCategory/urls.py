from django.urls import path
from . import views
urlpatterns=[
    path('subcatlist/',views.subCategory_list,name='subCategory_list'),
    path('subcatadd/',views.subCategory_add,name='subCategory_add'),
    path('subcatdelete/<str:pk>/',views.subCategory_delete,name='subCategory_delete'),
    path('subcatedit/<str:pk>/',views.subCategory_edit,name='subCategory_edit'),
]
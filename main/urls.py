from django.urls import path

from main import views

urlpatterns=[
    path('',views.home, name = 'home'),
    path('about/',views.about,name='about'),
    path('category/',views.category,name='category'),
    path('news/',views.news,name='news'),
    path('panel/',views.panel,name='panel'),
    path('login/',views.my_login,name='my_login'),
    path('logout/',views.log_out,name='log_out'),
    path('setting/',views.site_setting,name='site_setting'),
    path('contact/',views.contact,name='contact'),
    path('message/',views.message,name='message'),
    path('viewmessage/<str:pk>/',views.view_message,name='view_message'),
]
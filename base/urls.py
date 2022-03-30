from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name = 'home'),
    path('signin/',views.signin,name = 'signin'),
    path('signout/',views.signout,name = 'signout'),
    path('register/',views.register,name = 'register'),
    path('vendor/',views.vendor,name = 'vendor'),
    path('profile/',views.profile,name = 'profile'),
]
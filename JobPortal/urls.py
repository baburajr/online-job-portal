from dango.urls import path
from .views import *


urlpatterns=[
    path('',home,name='home'),
    path('login.html/',loginUser,name='login'),
    path('logout.html/',logoutUser,name='logout'),
    path('register.html/',registerUser,name='register'),
    path('apply.html/',applyPage,name='apply'),
]
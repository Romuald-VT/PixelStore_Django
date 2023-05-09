from django.urls import path 
from .views import register,login,logout,forgot_password

urlpatterns = [
    path('register/',register,name='register'),
    path('login/', login,name='login'),
    path('logout/',logout,name='logout'),
    path('forgotPassword/',forgot_password,name='forgot_password'),
]

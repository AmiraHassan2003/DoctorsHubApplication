from django.urls import path
from . import views

urlpatterns = [
    path('', views.logIn, name="login"),
    path('signUp', views.signUp, name="signup"),
    path('logOut', views.logOut, name="logout"),
    path('index/<int:user_id>/', views.Home, name='home'),
]
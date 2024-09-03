from django.urls import path
from . import views

urlpatterns = [
    path('', views.specialization, name="specialization"),
    path('doctor/', views.show_Doctors, name="show_Doctors"),
    path('<int:doctor_id>/', views.show_doctor_info, name="show_doctor_info"),

]
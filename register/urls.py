from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('book_appointment/', views.book_appointment, name='book_appointment'),
    path('appointment_details/<int:appointment_id>/', views.appointment_details, name='appointment_details'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('verification_email/', views.verification_email, name='verification_email'),
    path('reset_password/', views.reset_password, name='reset_password'),
    path('verify_reset_code/', views.verify_reset_code, name='verify_reset_code'),
]

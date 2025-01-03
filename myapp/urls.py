from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('forgot-user-id/', views.forgot_user_id_view, name='forgot_user_id'),
    path('verify-code/', views.verify_code, name='verify_code'),
    path('forgot-password/', views.forgot_password_view, name='forgot_password'),
    path('verify-password/', views.verify_password, name='verify_password'),
    path('set-password/', views.set_password, name='set_password'),
   
]

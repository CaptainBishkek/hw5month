from django.urls import path
from . import views

app_name = 'your_app_name'

urlpatterns = [
    path('register/', views.UserRegistrationAPIView.as_view(), name='user-registration'),
    path('confirm/', views.ConfirmUserAPIView.as_view(), name='confirm-user'),
    path('login/', views.UserLoginAPIView.as_view(), name='user-login'),
]

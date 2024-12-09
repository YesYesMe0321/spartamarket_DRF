from django.urls import path
from .views import RegisterView, LoginView, ProfileView

urlpatterns = [
    path('', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('<str:username>/', ProfileView.as_view(), name='profile'),
]

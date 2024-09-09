from django.urls import path
from .views import RegisterView, ProfileView

urlpatterns = [
    path('', RegisterView.as_view(), name='register'),
    path('<str:username>/', ProfileView.as_view(), name='profile'),
]

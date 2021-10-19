from django.urls import path
from .views import UserDetail , ProfileDetail

app_name = 'user'

urlpatterns = [
    path('', UserDetail.as_view(), name='user_detail'),
    path('profile/<int:pk>/', ProfileDetail.as_view(), name='profile_detail'),
]
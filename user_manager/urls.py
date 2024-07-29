from django.urls import path
from .views import UserCreateView, UserDetailView

urlpatterns = [
    path('create/', UserCreateView.as_view(), name='create-user'),
    path('<int:pk>/', UserDetailView.as_view(), name='user-detail'),
]

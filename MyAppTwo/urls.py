from django.urls import path
from MyAppTwo import views

urlpatterns = [
    path('', views.index, name="index"),
    path('users/', views.users, name="users")
]

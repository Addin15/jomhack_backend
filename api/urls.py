
from django.urls import path
from . import views
from knox import views as knox

urlpatterns = [
    path('register/', views.register),
    path('login/', views.login),
    path('logout/', knox.LogoutView.as_view()),
    path('logoutall/', knox.LogoutAllView.as_view()),
]

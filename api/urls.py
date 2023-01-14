
from django.urls import path
from . import views
from knox import views as knox

urlpatterns = [
    path('register/', views.register),
    path('login/', views.login),
    path('user/', views.user),
    path('edit/', views.edit),
    path('logout/', knox.LogoutView.as_view()),
    path('logoutall/', knox.LogoutAllView.as_view()),
    # plans
    path('plans/', views.plans),
    path('user/plans/', views.user_plans),
    #
    path('user/news/', views.news),
]

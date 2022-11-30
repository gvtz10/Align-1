from django.urls import path
from . import views

urlpatterns = [
    path('home', views.HomeView.as_view(), name='home'),
    path('signup', views.user_signup, name='signup'),
    path('login', views.user_login, name='login'),
    path('proj', views.ProjectView.as_view(), name='proj'),
    path('act', views.ProjectView.as_view(), name='act'),
]


# candidate/urls.py
from django.urls import path, reverse_lazy
from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views
from .views import register


urlpatterns = [
    path('register/', register, name='register'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('home')), name='logout'),
    path('', views.user_login, name='user_login'),  # Default login page
    path('home/', views.home, name='home'),
    path('login/', views.user_login, name='login'),  # Use a consistent name for the login URL
    path('page1/', views.page, {'poll_id': 1}, name='page1'),
    path('page2/', views.page, {'poll_id': 2}, name='page2'),
    path('page3/', views.page, {'poll_id': 3}, name='page3'),
    path('poll/<int:poll_id>/', views.poll, name='poll'),
    path('vote/<int:poll_id>/', views.vote, name='vote'),
]


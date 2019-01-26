from django.urls import path
from . import views

urlpatterns = [
    path('', views.render_rsvp, name='render_rsvp'),
    path('guest/', views.render_auth_rsvp, name='user_login_rsvp'),
  
]
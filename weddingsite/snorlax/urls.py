from django.urls import path
from . import views

urlpatterns = [
    path('', views.do_rsvp, name='do_rsvp'),
]
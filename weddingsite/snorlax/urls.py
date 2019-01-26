from django.urls import path
from . import views

urlpatterns = [
    path('', views.render_rsvp, name='render_rsvp'),
    path('do/', views.do_rsvp, name='do_rsvp'),
]
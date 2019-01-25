"""weddingsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include, handler404, handler500
from django.conf.urls.i18n import i18n_patterns

urlpatterns = i18n_patterns(
    path('rsvp/', include('snorlax.urls')),
)


urlpatterns += i18n_patterns(
	#Django Admin
	url(r'^admin/', admin.site.urls),
)

handler404 = 'snorlax.views.view_404'
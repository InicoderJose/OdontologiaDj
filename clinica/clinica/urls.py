"""clinica URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
#from applications.home.models import datos
from django.conf.urls import handler404, handler500
from applications.home.views import Error404view, Error405view


urlpatterns = [
    path('admin/', admin.site.urls, {'extra_context': {'mycontext': ''}}),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('applications.home.urls')),
    path('', include('applications.empresa.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = Error404view.as_view()
handler500 = Error405view.as_view()
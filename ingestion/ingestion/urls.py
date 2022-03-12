"""ingestion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from . import views

admin.site.site_header = "Srishti Admin Portal"

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^accounts/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name='login.html'), name='logout'),
    url(r'^upload_file/$', views.upload_files, name='upload_files'),
    url(r'^render_mapping/$', views.render_mapping, name='render_mapping'),
    url(r'^save_mapping/$', views.save_mapping, name='save_mapping'),
    url('^upload_menu/$', TemplateView.as_view(template_name='upload_menu.html'), name='upload'),
    url(r'^edit_menu/$',views.LeadsTableView.as_view(),name='edit_menu'),
    url('', TemplateView.as_view(template_name='home.html'), name='home')
]

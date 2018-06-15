"""mysite URL Configuration

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
from django.urls import include, path
from django.contrib.auth import views as auth_views
from blog import views as blog_views
from cadmin import views as cadmin_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.flatpages import views as flat_views
from django.contrib.sitemaps.views import sitemap
from blog.sitemap import PostSitemap

sitemaps = {'posts': PostSitemap}

urlpatterns = [
  path('register/', cadmin_views.register, name='register'),
  path('', include('myauth.urls')),
  path('polls/', include('polls.urls')),
  path('admin/', admin.site.urls),
  path('create/', include('cadmin.urls')),
  path('blog/', include('blog.urls')),
  path('feedback/', blog_views.feedback, name='feedback'),
  path('blog_login/', blog_views.login, name='blog_login'),
  path('login/',cadmin_views.login, {'template_name': 'cadmin/login.html'}, name='login'),
  path('blog_logout/', blog_views.logout, name='blog_logout'),
  path('logout/', auth_views.logout, {'template_name': 'cadmin/logout.html'}, name='logout'),
  path('admin_page/', blog_views.admin_page, name='admin_page'),
  path('about/', flat_views.flatpage, {'url': '/about/'}, name='about'),
  path('eula/', flat_views.flatpage, {'url': '/eula/'}, name='eula'),
  path('sitemap.xml/', sitemap, {'sitemaps' : sitemaps } , name='sitemap'),
  path('account-info/', cadmin_views.account_info, name='account_info'),
  path('password-change-done/', auth_views.password_change_done, {'template_name': 'cadmin/password_change_done.html'}, name='password_change_done' ),
  path('password-change/', auth_views.password_change, {'template_name': 'cadmin/password_change.html' , 'post_change_redirect': 'password_change_done'}, name='password_change'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""
URL configuration for WebBooks project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, re_path, include
from catalog import views
from django.contrib.auth.views import LogoutView
from .settings import LOGOUT_REDIRECT_URL

urlpatterns = [
    path('catalog/authors/<id>', views.authors),
    re_path(r'^authors/$', views.AuthorsListView.as_view(), name='authors'),
    re_path(r'^books/$', views.BookListView.as_view(), name='books'),
    re_path(r'^books/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='books-detail'),
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),

]

urlpatterns += [
    #path('accounts/', include("accounts.urls", namespace="accounts")),
    #re_path(r'^logout/$', LogoutView.as_view(), {'next_page': LOGOUT_REDIRECT_URL}, name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),

]

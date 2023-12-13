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

urlpatterns = [
    path('edit1/<int:id>', views.edit1, name="edit1"),
    path('create/', views.create, name='create'),
    path('delete/<int:id>', views.delete, name="delete"),

    path('catalog/authors/<id>', views.authors),
    re_path(r'^authors/$', views.AuthorsListView.as_view(), name='authors'),
    re_path(r'^books/$', views.BookListView.as_view(), name='books'),
    re_path(r'^books/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='books-detail'),
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),

]

urlpatterns += [
    path('accounts/logout/', views.logout_view, name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
    re_path(r'^mybooks/$', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path('authors_add/', views.authors_add, name='authors_add'),

    re_path(r'^books/create/$', views.BooksCreate.as_view(), name='books_create'),
    re_path(r'^books/update/(?P<pk>\d+)$', views.BooksUpdate.as_view(), name='books_update'),
    re_path(r'^books/delete/(?P<pk>\d+)$', views.BooksDelete.as_view(), name='books_delete'),
]

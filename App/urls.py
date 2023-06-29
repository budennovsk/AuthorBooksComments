"""
URL configuration for AuthorBooksComments project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from django.urls import path

from App import views

urlpatterns = [
    path("", views.all, name='all'),
    path("loginup", views.loginup, name='loginup'),
    path("inlogin", views.inlogin, name='inlogin'),
    path("logoutuser", views.logoutuser, name='logoutuser'),
    path("<int:author_id>/", views.get_list_books, name='get_list_books'),
    path("/<int:book_id>/", views.get_book, name='get_book'),
    path("/<int:book_id_delete>/delete", views.delete, name='delete'),
    path("<int:comment_id>/comments", views.get_comment, name='get_comment'),
    path("<int:comment_id>/comments/update_id", views.update_comments, name='update_comments'),
]

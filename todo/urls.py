"""todo URL Configuration

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
from django.urls import path
from main.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),#урок
    path('', homepage, name="home"),#урок
    path ("test/", test, name="test"),#урок
    path("test2/", test2, name="test2"),#урок
    path("add-todo/", add_todo, name="add-todo"),#урок
    path("delete-todo/<id>/", delete_todo, name="delete-todo"),#урок
    path("mark-todo/<id>/", mark_todo, name="mark-todo"),#урок
    path("unmark-todo/<id>/", unmark_todo, name="unmark-todo"),#дз
    path("close-todo/<id>/", close_todo, name="close-todo"),#урок
    path("add-tomeet/", add_tomeet, name="add-tomeet"),#дз
    path("delete-tomeet/<id>/", delete_tomeet, name="delete-tomeet"), #Создайте функцию delete_to_meet для модели ToMeet и подключите ее к кнопке удалить.
    path("mark-tomeet/<id>/", mark_tomeet, name="mark-tomeet"),     #Создайте функцию mark_to_meet для модели ToMeet. (урок 31) Подключите ее к подходящей кнопке.
    path("unmark-tomeet/<id>/", unmark_tomeet, name="unmark-tomeet"),#дз
    path("close-tomeet/<id>/", close_tomeet, name="close-tomeet"),#дз
    path("habit1/", habit1, name="habit1"), #дз
    path("add-habits/", add_habits, name="add-habits"), #дз
]   + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


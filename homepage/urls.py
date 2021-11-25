from django.urls import path,include
from . import views

app_name = 'homepage'
urlpatterns = [
    path('', views.home , name = "home"),
    path('change_language/<pk>', views.change_language , name = "change_language"),
]

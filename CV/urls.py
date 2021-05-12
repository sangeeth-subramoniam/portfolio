from django.urls import path,include
from . import views

app_name = 'CV'
urlpatterns = [
    path('', views.home , name = "home"),
]

from django.urls import path,include
from . import views

app_name = 'CV'
urlpatterns = [
    path('', views.home , name = "home"),
    path('about/', views.about , name = "about"),
    path('linktree/', views.linktree , name = "linktree"),
    path('resume/', views.resume , name = "resume"),
    path('projects/', views.projects , name = "projects"),
    path('others/', views.others , name = "others"),
]

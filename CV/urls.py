from django.urls import path,include
from . import views

app_name = 'CV'
urlpatterns = [
    path('', views.home , name = "home"),
    path('/education', views.education , name = "education"),
    path('/schooldetail', views.schooldetail , name = "schooldetail"),
    path('/collegedetail', views.collegedetail , name = "collegedetail"),
]

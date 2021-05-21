from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'cv/home.html')


def education(request):
    return render(request,'CV/education.html')

def schooldetail(request):
    return render(request,'detail/schooldetail.html')

def collegedetail(request):
    return render(request,'detail/collegedetail.html')
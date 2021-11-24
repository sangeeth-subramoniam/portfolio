from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'cv/home.html')

def about(request):
    context = {
        "page" : 1,

    }
    return render(request, 'cv/about.html' , context)


def linktree(request):
    context = {
        "page" : 2,
        "twitter" : "https:www.twitter.com",
        "linkedin" : "https://www.linkedin.com",
        "instagram" : "https://www.instagram.com",
        "github" : "https://www.github.com",
        "stackoverflow" : "https://www.stackoverflow.com"
    }
    return render(request,'cv/linktree.html' , context)


def resume(request):
    context = {
        "page" : 3,

    }
    return render(request, 'cv/resume.html' , context)


def projects(request):
    context = {
        "page" : 4,

    }
    return render(request, 'cv/projects.html' , context)

def others(request):
    context = {
        "page" : 5,

    }
    return render(request, 'cv/others.html' , context)
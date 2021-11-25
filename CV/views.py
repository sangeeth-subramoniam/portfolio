from django.shortcuts import redirect, render

# Create your views here.
def about(request):

    if 'lang' not in request.session:
        #setting initial session value to en
        request.session['lang'] = 'en'

    context = {
        "page" : 1,

    }
    
    if request.session['lang'] == "jp":
        return render(request,'CV/about_japanese.html' , context)
    else:
        return render(request,'CV/about.html' , context)

def linktree(request):
    if 'lang' not in request.session:
        #setting initial session value to en
        request.session['lang'] = 'en'

    context = {
        "page" : 2,
        "twitter" : "https://twitter.com/sangeethsubram5?lang=en",
        "linkedin" : "https://www.linkedin.com/in/sangeeth-subramoniam-358106127/?originalSubdomain=jp",
        "instagram" : "https://www.instagram.com/sangeeth_subramoniam/?hl=en",
        "github" : "https://github.com/sangeeth-subramoniam",
        "stackoverflow" : "https://stackoverflow.com/users/8401179/sangeeth-subramoniam"
    }
    if request.session['lang'] == "jp":
        return render(request,'CV/linktree_japanese.html' , context)
    else:
        return render(request,'CV/linktree.html' , context)


def resume(request):
    context = {
        "page" : 3,

    }
    if request.session['lang'] == "jp":
        return render(request,'CV/resume_japanese.html' , context)
    else:
        return render(request,'CV/resume.html' , context)


def projects(request):
    context = {
        "page" : 4,

    }
    if request.session['lang'] == "jp":
        return render(request,'CV/projects_japanese.html' , context)
    else:
        return render(request,'CV/projects.html' , context)

def others(request):
    context = {
        "page" : 5,

    }
    if request.session['lang'] == "jp":
        return render(request, 'CV/others_japanese.html' , context)
    else:
        return render(request, 'CV/others.html' , context)

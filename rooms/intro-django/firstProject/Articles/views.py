from django.shortcuts import HttpResponse, render

# Create your views here.

def hello(request):
#    # HARDCODING IS NOT RECOMMENDED!
#    text = """<h1>Welcome to my Articles app!</h1>"""
#    return HttpResponse(text)
    # Map user-created templates/hello.html
    return render(request, "Articles/template/hello.html")

# Called from urls.py > urlpatterns > path > views.index
def index(request):
    #return HttpResponse("Hello, World!")

    # Automatically *render* your template from index.html
    return render(request, 'index.html')


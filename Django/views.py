from django.http import HttpResponse

def home(request):
    return HttpResponse("home page")

def about(request):
    return HttpResponse("about page")

def contact(request):
    return HttpResponse("contact page")

 
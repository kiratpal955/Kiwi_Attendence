from django.shortcuts import render

# Create your views here.

def AdminLogin(request):
    return render(request, "admin.html")
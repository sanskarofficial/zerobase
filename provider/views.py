from django.shortcuts import render

def index(request):
    context = {}
    return render(request, "frontend/provider/home.html")

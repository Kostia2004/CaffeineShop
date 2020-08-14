from django.shortcuts import render


def index(request):
    return render(request=request, template_name="shop/index.html")

def login(request):
    return render(request=request, template_name="shop/login.html")
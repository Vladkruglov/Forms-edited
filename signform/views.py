from django.http import HttpResponse
from django.shortcuts import render

def nosign(request):
    return HttpResponse("Вы не зарегистрированы!")

def signin(request):
    if request.GET.get("nic") != "" and request.GET.get("password") != "":
        print("Hello, {}".format(request.GET.get("nic")))
    return HttpResponse("Вы на странице входа в аккаунт")
    

def signup(request):
    if request.GET.get("nic") != "" and request.GET.get("password") != "" and request.GET.get("passwordcheck") != "" and request.GET.get("password") == request.GET.get("passwordcheck"):
        print("Hello, {}".format(request.GET.get("nic")))
    return HttpResponse("Вы на странице регистрации")

def signokay(request):
    if request.GET.get("name") != "" and request.GET.get("secname") != "":
        print("Hello, {} {}".format(request.GET.get("name"), request.GET.get("secname")))
    return HttpResponse("Вы зашли!")


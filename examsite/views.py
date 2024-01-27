from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,"index.html")
def login(request):
    return render(request,"login.html")
def startexam(request):
    return render(request,"stexam.html")
def q1(request):
    return render(request,"q1.html")
def q2(request):
    return render(request,"q2.html")
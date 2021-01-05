from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("안녕 장고야~~~")

def page(request):
    return HttpResponse("좋은 페이지에 들어왔다")
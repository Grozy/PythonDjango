#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
import json
# Create your views here.
def index(request):
	return HttpResponse(u"欢迎光临 Sng's Blog")
def add(request):
	a = request.GET["a"]
	b = request.GET["b"]
	c = int(a) + int(b)
	return HttpResponse(str(c))
def userInfo(request):
	dict = {}
	dict ["name"] = "孙国志"
	dict ["uid"] = 19910313
	dict ["age"] = 25
	return HttpResponse(json.dumps(dict),content_type="application/json")
def add2(request,a,b):
	c = int(a) + int(b)
	return HttpResponse(json.dumps(str(c)),content_type="application/json")

#home page
def home(request):
	return render(request, 'index.html')

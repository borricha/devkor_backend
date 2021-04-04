from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    if request.method == "GET":
       # response.status_code = 200
        return HttpResponse("{\"req_method\":\"get\"}")
    elif request.method == "POST":
       # response.status_code = 200
        return HttpResponse("{\"req_method\":\'post\"}")
    else:
        HttpResponse.status_code = 405
        return HttpResponse("{\"error\":\"request method not allowed\"}")

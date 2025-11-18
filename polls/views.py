#importing http class ... pull data from db also transform 
#request handler

from django.http import HttpResponse #importing http class 
from django.shortcuts import render#importing render function to render html template


#-------------------------
#HTTP object : request 
#To get to know the details about request made 
#To get info on console

# def index(request):
#     print("Method:", request.method)
#     print("Path:", request.path)
#     print("GET params:", request.GET)
#     print("POST data:", request.POST)
#     print("Cookies:", request.COOKIES)
#     print("Headers:", request.META)  
#     return HttpResponse("Check console")

#-------------------------


#map the view to URL.When request came then URL mapped to view.
def index(request):
    #HTTPResponse is an instance of httpResponse class 
    #return HttpResponse("Hello, world. You're at the polls index.")
    x = 1
    y = 2
    #render function (request object which is type of http repsone , template name , optional(dynamic mapping of object))
    return render(request , 'hello.html', {'name' : 'Ghazia'})


#adding two numbers
def add(request):

    val1 = int(request.POST['num1'])#getting response from server in the form of object "request"
    val2 = int(request.POST['num2'])#fetch/get values form server  .... vlaues got saved in variables hmtlfiel
    res = val1 + val2

    return render(request, 'result.html' , {'result':res})

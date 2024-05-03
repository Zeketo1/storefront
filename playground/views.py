from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# request -> response
# request handler
# action

def calculate():
    x = 1
    y = 2
    return x

def say_hello(request):
    # You can Pull data from a database
    # Transform data
    # Send emails

    # Using HttpResponse ->
    # return HttpResponse('Hello World')

    x = calculate()
    return render(request, 'hello.html', {'name': 'Francis'})
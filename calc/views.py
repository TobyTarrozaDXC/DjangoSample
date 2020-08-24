# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render




def home(request):
    return render(request, 'home2.html', {'name':"Alison"})
def add(request):

    val1 = request.GET['num1']
    val2 = request.GET['num2']
    res = int(val1) + int(val2)


    return render(request, 'result.html', {'result':res})

def dummy(request):
    return HttpResponse("dummy page")
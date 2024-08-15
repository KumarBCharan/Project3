from django.shortcuts import render

from django.http import HttpResponse

def html(request):
    return render(request ,'collegelinks.html')

def html1(request):
    return render (request,'aboutus.html')

def html2(request):
    return render (request,'courses.html')

def html3(request):
    return render (request,'contactus.html')
def html4(request):
    return render (request,'facilities.html')
def html5(request):
    return render (request,'fee.html')

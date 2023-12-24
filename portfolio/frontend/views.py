from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse(
        '''<h1 style="font-family:fantasy;
        padding: 355px 0;
        text-align: center;">server started</h1>'''
    )

def portfolio(request):
    return render(request,'frontend/index.html')

def submitform(request):
    return render(request,'frontend/submitform.html')




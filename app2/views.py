from django.shortcuts import render

# Create your views here.
def chinni(request):
    return render(request,'hello.html')

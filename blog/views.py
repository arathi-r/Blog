from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Person
# Create your views here.
def plist(request):
    number=Person.objects.get(first_name='arathi')
    text = "<h1>welcome to my app number %s  !</h1>"% number.first_name
    return HttpResponse(text)

def pcal(request):
    cal = Person.objects.all()
    context={'instances':cal}
    return render(request,'home.html',context)
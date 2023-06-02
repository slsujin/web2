

# Create your views here.
from django.shortcuts import render,HttpResponse

from .models import travel1


# Create your views here.
def web1(request):
    obj=travel1.objects.all()
    return render(request,"index.html",{'result':obj})



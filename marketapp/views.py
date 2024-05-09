from django.shortcuts import render
from .models import *

# Create your views here
def index(request):
    items = item.objects.filter(is_sold=False)[0:6]
    categories = category.objects.all()
    context = {
        'categories': categories,
        'items':items,
    }
    return render(request,'index.html',context)

def contact(request):
    return render(request,"contact.html")
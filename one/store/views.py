from django.shortcuts import render
from .models import Geek
# Create your views here.
def product(requst):
    product = Geek.objects.all()
    context  = {
        'product':product
    }
    return render(requst,'store/home.html', context)








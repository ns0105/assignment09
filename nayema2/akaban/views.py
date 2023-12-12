from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def an(request):
    return render(request, 'akaban/an.html',)
def An_Home(request):
    return render(request, 'akaban/home.html')
def An_Account(request):
    return render(request, 'akaban/account.html')
def An_Offers(request):
    return render(request, 'akaban/offers.html')
#Categories:
def Best_sellers(request):
    return render(request, 'akaban/bestsellers.html')


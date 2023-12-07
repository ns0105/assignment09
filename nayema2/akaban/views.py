from django.shortcuts import render


# Create your views here.
def an(request):
    return render(request, 'akaban/an.html',)
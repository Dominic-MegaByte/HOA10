from django.shortcuts import render
from .models import Sign
from django.db.models import Q

def index(request):
    return render(request, 'home.html')

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about_me.html')

def know(request):
    return render(request, 'know_me_well.html')

def signs(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        signs = Sign.objects.filter( 
                Q(name__icontains=searched) |
                Q(months__icontains=searched) |
                Q(element__icontains=searched) |
                Q(symbol__icontains=searched) |
                Q(nickname__icontains=searched) |
                Q(modalities__icontains=searched)
            )
        return render(request, 'zodiac_signs.html', {'searched':searched, 'signs':signs})
    else:
        return render(request, 'zodiac_signs.html')
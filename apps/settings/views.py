from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'home2.html', locals())


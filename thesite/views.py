from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'thesite/home.html', {})


def postercreate(request):
	return render(request, 'thesite/postercreate.html', {})
from django.shortcuts import render, redirect
from MBTApp import mbtViews

def project(request):
    """Lista realizacji — delegacja do mbtViews.realizacje."""
    return mbtViews.realizacje(request)

def brandbook(request):
    """Widok Brand Booka."""
    return render(request, 'pages/111111.html')

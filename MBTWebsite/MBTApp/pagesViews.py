from django.shortcuts import redirect
from MBTApp import mbtViews


def project(request):
    """Lista realizacji — delegacja do mbtViews.realizacje."""
    return mbtViews.realizacje(request)

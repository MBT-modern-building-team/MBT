from django.shortcuts import render
from django.template import RequestContext

def handler404(request, exception, template_name='404.html'):
    context = {
        'title': 'Page Not Found',
        'error_code': 404,
        'error_message': 'The page you are looking for might have been removed or is temporarily unavailable.'
    }
    return render(request, template_name, context, status=404)

def handler500(request, template_name='404.html'):
    context = {
        'title': 'Server Error',
        'error_code': 500,
        'error_message': 'An error occurred while processing your request. Please try again later.'
    }
    return render(request, template_name, context, status=500)

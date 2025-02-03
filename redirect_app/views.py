from django.shortcuts import render
from django.urls import path
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import redirect

def redirect_view(request):
    html_content = """
    <html>
    <head>
        <meta http-equiv="refresh" content="5;url=https://rcselect.ifrc.org" />
    </head>
    <body>
        <h2>Redirecting...</h2>
        <p>RC Select has moved to <a href='https://rcselect.ifrc.org'>rcselect.ifrc.org</a>. You will be redirected in 5 seconds.</p>
        <p>If the redirection does not happen automatically, <a href='https://rcselect.ifrc.org'>click here</a>.</p>
    </body>
    </html>
    """
    return HttpResponse(html_content)

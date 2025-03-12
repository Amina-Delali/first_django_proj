from django.shortcuts import render

# Create your views here.

# def index(request):
#     return render(request, 'first/index.html')

from django.http import HttpResponse
from datetime import datetime


def index(request):
    now = datetime.now()
    html = f'''
    <html>
        <body>
            <h1>Hello from Vercel!</h1>
            <p>The current time is { now }.</p>
        </body>
    </html>
    '''
    return HttpResponse(html)
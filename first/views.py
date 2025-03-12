from django.shortcuts import render

# Create your views here.

# def index(request):
#     return render(request, 'first/index.html')

from datetime import datetime

from django.http import HttpResponse

def index(request):
    now = datetime.now()
    html = f'''
    <html>
        <body>
            <h1>Hello - this is the basic setup 😱</h1>
            <p>The current time is { now }---.</p>
        </body>
    </html>
    '''
    return HttpResponse(html)
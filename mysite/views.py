from django.http import HttpResponse, Http404
from datetime import datetime, timedelta
from django.shortcuts import render



def hello(request):
    return HttpResponse("Helo World")
    
    
def mydate(request):
    return HttpResponse(datetime.now())
    
    
def date_offset(request, offset):
    try:
        int_offset = int(offset)
    except ValueError:
        raise Http404()
    delta = timedelta(days=int_offset)
    new_date = datetime.now() + delta
    return render(request, "futuretime.html", {"new_date": new_date, "offset": offset})


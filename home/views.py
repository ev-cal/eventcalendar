from django.shortcuts import render
from . models import event
import datetime

def main(request):
    obj=event.objects.order_by('year','month','day')
    tod=datetime.date.today()
    formattedtod=tod.strftime("%d - %B  - %Y")
    day=tod.day
    month=tod.month
    year=tod.year
    print(tod)
    return render(request,"index.html",{'events':obj,'d':day,'m':month,'y':year,'t':tod,'ft':formattedtod})
def about(request):
    tod=datetime.date.today()
    year=tod.year
    return render(request,"about.html",{'y':year})
def feedback(request):
    tod=datetime.date.today()
    year=tod.year
    return render(request,"feedback.html",{'y':year})
def eventdetails(request,eventid):
    obj=event.objects.get(id=eventid)
    return render(request,"events.html",{'dts':obj})
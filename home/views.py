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
def filter(request):
    obj=event.objects.order_by('year','month','day')
    tod=datetime.date.today()
    if request.method=='POST':
        start=request.POST['start']
        end=request.POST['end']
        fs=datetime.datetime.strptime(start, "%Y-%m-%d").date()
        fe=datetime.datetime.strptime(end, "%Y-%m-%d").date()
    return render(request,"allevents.html",{'all':obj,'fs':fs,'fe':fe})



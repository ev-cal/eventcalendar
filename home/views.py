from django.shortcuts import render
from . models import event
import datetime

def main(request):
    obj=event.objects.order_by('year','month','day')
    tod=datetime.date.today()
    formattedtod=tod.strftime("%d - %B  - %Y")
    formattedmonth=tod.strftime("%B")
    formattedyear=tod.strftime("%Y")
    day=tod.day
    month=tod.month
    year=tod.year
    if request.method=="POST":
        month_input=request.POST['month_input']
        year_input=request.POST['year_input']
        if month_input=="January":
            mi=1
        elif month_input=="February":
            mi=2
        if month_input=="March":
            mi=3
        elif month_input=="April":
            mi=4
        if month_input=="May":
            mi=5
        elif month_input=="June":
            mi=6
        if month_input=="July":
            mi=7
        elif month_input=="August":
            mi=8
        if month_input=="September":
            mi=9
        elif month_input=="October":
            mi=10
        if month_input=="November":
            mi=11
        elif month_input=="December":
            mi=12
        yi=year_input
        formattedmonth=month_input
        formattedyear=int(yi)
        print(type(formattedyear))
        return render(request,"index.html",{'events':obj,'d':day,'m':month,'y':year,'t':tod,'ft':formattedtod,'mi':mi,'yi':yi,'fm':formattedmonth,'fy':formattedyear})

    return render(request,"index.html",{'events':obj,'d':day,'m':month,'y':year,'t':tod,'ft':formattedtod,'fm':formattedmonth,'fy':formattedyear})
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
def heroku(request):
    return render(request,"about.html")


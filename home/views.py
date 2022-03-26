from django.shortcuts import render,redirect
from . models import event, feedback as fbc ,comment
import datetime
from django.contrib.auth.models import User,auth
from django.http import HttpResponseRedirect

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
        return render(request,"index.html",{'events':obj,'d':day,'m':month,'y':year,'t':tod,'ft':formattedtod,'mi':mi,'yi':yi,'fm':formattedmonth,'fy':formattedyear})

    return render(request,"index.html",{'events':obj,'d':day,'m':month,'y':year,'t':tod,'ft':formattedtod,'fm':formattedmonth,'fy':formattedyear})
def about(request):
    tod=datetime.date.today()
    year=tod.year
    return render(request,"about.html",{'y':year})
def feedback(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        text=request.POST['message']
        fb=fbc(name=name,email=email,message=text)
        fb.save()
        return redirect('/')
    tod=datetime.date.today()
    year=tod.year
    return render(request,"feedback.html",{'y':year})
def eventdetails(request,eventid):
    obj=event.objects.get(id=eventid)
    obj1=comment.objects.filter(commentid=eventid)
    if request.method=="POST":
        name=request.POST.get('name')
        text=request.POST.get('comment')
        commentid1=request.POST.get('id')
        commentid=int(commentid1)
        cmt=comment(text=text,name=name,commentid=commentid)
        cmt.save()
    return render(request,"events.html",{'dts':obj,'cmt':obj1})
def filter(request):
    obj=event.objects.order_by('year','month','day')
    tod=datetime.date.today()
    if request.method=='POST':
        start=request.POST['start']
        end=request.POST['end']
        fs=datetime.datetime.strptime(start, "%Y-%m-%d").date()
        fe=datetime.datetime.strptime(end, "%Y-%m-%d").date()
    return render(request,"allevents.html",{'all':obj,'fs':fs,'fe':fe})
def delete(request,cmtid):
    if request.method=="POST":
        obj=comment.objects.get(id=cmtid)
        obj.delete()
        return redirect('/')
    return render(request,'delete.html')
def cancel(request):
    return redirect('/')


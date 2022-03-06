from django.shortcuts import render
from . models import event
import datetime

def main(request):
    obj=event.objects.all()
    tod=datetime.date.today()
    day=tod.day
    month=tod.month
    year=tod.year-2000
    print(year)
    return render(request,"index.html",{'events':obj,'d':day,'m':month,'y':year})
def about(request):
    return render(request,"about.html")
def feedback(request):
    return render(request,"feedback.html")

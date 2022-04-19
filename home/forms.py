from django import forms
from . models import event

class updateform(forms.ModelForm):
    class Meta:
        model = event
        fields=['name','day','month','year','decs','time','venue','date','weblink']
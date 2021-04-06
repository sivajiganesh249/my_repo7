from django.shortcuts import render
from . import forms
# Create your views here.
def StudentRegisterview(request):
    form=forms.StudentRegistration()
    return render(request,'testapp/register.html',{'form':form})

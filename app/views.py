from django.shortcuts import render
from app.forms import *
from app.models import *
from django.http import HttpResponse
# Create your views here.
def membership(request):
    MO=MembershipForm()
    d={'MO':MO}
    if request.method=='POST':
        MOD=MembershipForm(request.POST)
        if MOD.is_valid():
            package=MOD.cleaned_data['package']
            amount=MOD.cleaned_data['amount']
            MON=Membership.objects.get_or_create(package=package,amount=amount)[0]
            MON.save()
            return HttpResponse('submitted membership packages')
    return render(request,'membership.html',d)

def display(request):
    data=Membership.objects.all()
    d={'data':data}
    return render(request,'membership_data.html',d)




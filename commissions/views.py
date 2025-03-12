from django.shortcuts import render
from .models import Commissions, Comment

def commission_list(request):
    return render(request, 'commissions/commission_list.html', {"commission_list": Commissions.objects.all()})

def commission_detail(request, commission_id):
    commission = Commissions.objects.filter(id=commission_id).first()  
    comments = Comment.objects.filter(commission=commission)
    return render(request, 'commissions/commission_detail.html', {"commission": commission, "comments": comments})
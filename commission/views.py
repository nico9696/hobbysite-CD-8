from django.shortcuts import render
from .models import Commission, Comment

def commission_list(request):
    return render(request, 'commission/commission_list.html', {"commission_list": Commission.objects.all()})

def commission_detail(request, commission_id):
    commission = Commission.objects.filter(id=commission_id).first()  
    comments = Comment.objects.filter(commission=commission)
    return render(request, 'commission/commission_detail.html', {"commission": commission, "comments": comments})
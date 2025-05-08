from django.shortcuts import render
from .models import Commission, Job, JobApplication, Profile
from django.db.models import Case, When, Value, IntegerField

def commission_list(request):
    user = request.user

    created_by_user = []
    applied_by_user = []

    if user.is_authenticated:
        created_by_user = Commission.objects.filter(author=user)
        applied_by_user = Commission.objects.filter(jobapplication__applicant=user)


    status_order = Case(
        When(status='Open', then=Value(0)),
        When(status='Full', then=Value(1)),
        When(status='Completed', then=Value(2)),
        When(status='Discontinued', then=Value(3)),
        output_field=IntegerField()
    )

    commissions = Commission.objects.annotate(status_order=status_order).order_by('status_order', '-created_on')
    
    return render(request, 'commissions/commission_list.html', {"commission_list": commissions, "created_by_user": created_by_user, "applied_by_user": applied_by_user,})



def commission_detail(request, commission_id):
    commission = Commission.objects.filter(id=commission_id).first()  
    comments = Comment.objects.filter(commission=commission)
    return render(request, 'commissions/commission_detail.html', {"commission": commission, "comments": comments})
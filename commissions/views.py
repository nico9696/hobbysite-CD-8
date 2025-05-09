from django.shortcuts import render
from .models import Commission, Job, JobApplication, Profile
from django.db.models import Case, When, Value, IntegerField

def commission_list(request):
    user = request.user

    created_by_user = []
    applied_by_user = []

    if user.is_authenticated:
        created_by_user = Commission.objects.filter(author=user)
        applied_by_user = Commission.objects.filter(job__jobapplication__applicant=user.profile).distinct()

    status_order = Case(
        When(status='Open', then=Value(0)),
        When(status='Full', then=Value(1)),
        When(status='Completed', then=Value(2)),
        When(status='Discontinued', then=Value(3)),
        output_field=IntegerField()
    )

    commissions = Commission.objects.annotate(status_order=status_order).order_by('status_order', '-created_on')

    ctx = {
        "created_by_user": created_by_user, 
        "applied_by_user": applied_by_user,
        "commission_list": commissions,
    }
    
    return render(request, 'commissions/commission_list.html', ctx)

def commission_detail(request, commission_id):
    commission = Commission.objects.filter(id=commission_id).first()
    jobs = Job.objects.filter(commission=commission)

    job_details = []
    for job in jobs:
        accepted_applicants = JobApplication.objects.filter(job=job, status='Accepted').count()
        open_manpower = job.people_required - accepted_applicants

        job_details.append({
            'job': job,
            'open_manpower': open_manpower
        })

    ctx = {
        "commission": commission,
        "job_details": job_details,
    }
    
    return render(request, 'commissions/commission_detail.html', ctx)
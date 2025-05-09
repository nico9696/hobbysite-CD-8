from django.shortcuts import render, redirect
from .models import Commission, Job, JobApplication, Profile
from django.db.models import Case, When, Value, IntegerField
from django.contrib.auth.decorators import login_required
from .forms import CommissionForm, JobForm, JobApplicationForm, JobApplicantsForm

def commission_list(request):
    user = request.user

    created_by_user = []
    applied_by_user = []

    if user.is_authenticated:
        created_by_user = Commission.objects.filter(author=user.profile)
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
    sum_manpower = 0
    sum_open_manpower = 0

    job_details = []
    for job in jobs:
        accepted_applicants = JobApplication.objects.filter(job=job, status='Accepted').count()
        open_manpower = job.people_required - accepted_applicants
        sum_manpower += job.people_required
        sum_open_manpower += open_manpower

        job_application = JobApplication.objects.filter(job=job, applicant=request.user.profile).first()


        job_details.append({
            'job': job,
            'open_manpower': open_manpower,
            'accepted_applicants': accepted_applicants,
            'job_application': job_application,
        })

    if request.method == 'POST':
            job_id = request.POST.get('job_id')
            job = Job.objects.filter(id=job_id).first()

            if job:
                existing_application = JobApplication.objects.filter(job=job, applicant=request.user.profile).first()
                if not existing_application:
                    JobApplication.objects.create(job=job, applicant=request.user.profile, status='Pending')


            return redirect('commission_detail', commission_id=commission.id)

    ctx = {
        "commission": commission,
        "job_details": job_details,
        "sum_manpower" : sum_manpower,
        "sum_open_manpower" : sum_open_manpower
    }
    
    return render(request, 'commissions/commission_detail.html', ctx)

@login_required
def commission_create(request):
    if request.method == "POST":
        commission_form = CommissionForm(request.POST)
        if commission_form.is_valid():
            commission = commission_form.save(commit=False)
            commission.author = request.user.profile
            commission.save()
            return redirect('commission_detail', commission_id=commission.id)
    else:
        commission_form = CommissionForm()

    ctx = {
        'commission_form': commission_form
    }

    return render(request, 'commissions/commission_form.html', ctx)

@login_required
def commission_update(request, commission_id):
    commission = Commission.objects.filter(id=commission_id).first()

    if request.method == 'POST':
        commission_form = CommissionForm(request.POST, instance=commission)
        job_form = JobForm(request.POST)

        if commission_form.is_valid():
            commission_form.save()

            if job_form.is_valid() and any(job_form.cleaned_data.values()):
                job = job_form.save(commit=False)
                job.commission = commission
                job.save()

            jobs = Job.objects.filter(commission=commission)
            if jobs.exists() and all(job.status == 'Full' for job in jobs):
                commission.status = 'Full'
                commission.save()

            return redirect('commission_detail', commission_id=commission.id)
    else:
        commission_form = CommissionForm(instance=commission)
        job_form = JobForm()

    jobs = Job.objects.filter(commission=commission)

    ctx = {
        'commission_form': commission_form,
        'job_form': job_form,
        'jobs': jobs,
        'commission': commission
    }

    return render(request, 'commissions/commission_form.html', ctx)

@login_required
def job_create(request, commission_id):
    commission = Commission.objects.filter(id=commission_id).first()

    if request.method == "POST":
        job_form = JobForm(request.POST)
        if job_form.is_valid():
            job = job_form.save(commit=False)
            job.commission = commission
            job.save()
            return redirect('commission_detail', commission_id=commission.id)
    else:
        job_form = JobForm()

    ctx = {
        'job_form': job_form,
        'commission': commission
    }

    return render(request, 'commissions/job_create.html', ctx)
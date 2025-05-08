from django.db import models
from user_management.models import Profile

class Commission(models.Model):
    author =  models.ForeignKey(Profile,on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    STATUS_CHOICES = [
    ('Open', 'Open'),
    ('Full', 'Full'),
    ('Completed', 'Completed'),
    ('Discontinued', 'Discontinued'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Open')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
         return self.title
    
    class Meta:
          ordering = ['created_on']
          verbose_name = "Commission"
          verbose_name_plural = "Commissions" 

class Job(models.Model):
    commission = models.ForeignKey(Commission,on_delete=models.CASCADE)
    role =  models.CharField(max_length=255)
    people_required = models.PositiveIntegerField()
    STATUS_CHOICES = [
    ('Open', 'Open'),
    ('Full', 'Full'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Open')
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
         return f"Job: {self.role} for {self.commission.title}"
    
    class Meta:
          ordering = ['status', '-people_required', 'role']
          verbose_name = "Job"
          verbose_name_plural = "Jobs" 

class JobApplication(models.Model):
    job = models.ForeignKey(Job,on_delete=models.CASCADE)
    applicant =  models.ForeignKey(Profile,on_delete=models.CASCADE)
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    applied_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Application for {self.job.role} by {self.applicant}"
    
    class Meta:
          ordering = ['status', '-applied_on']
          verbose_name = "Job Applicant"
          verbose_name_plural = "Job Applicants" 
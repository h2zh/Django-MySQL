from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone

# types
class user_type(models.TextChoices):
    JOB_SEEKER = 'JobSeeker'
    RECRUITER = 'Recruiter'

# types
class job_status(models.TextChoices):
    PENDING = 'Pending'
    INTERVIEWED = 'Interviewed'
    REJECTED = 'Rejected'
    ACCEPTED = 'Accepted'

#User Model
class User(models.Model):
    email = models.EmailField(unique=True, null=False)
    password = models.CharField(max_length=255, null=False)
    type = models.CharField(max_length=255, choices=user_type.choices, null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)

# Employer Model
class Employer(models.Model):
    employer = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=255, unique=True, null=False)

#Job model
class Job(models.Model):
    employer = models.ForeignKey(Employer, to_field='name',on_delete=models.CASCADE, null=False,db_column='employer_name')
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)
    job_title = models.CharField(max_length=255, null=False)
    description = models.TextField(null=False)
    qualification = models.TextField(blank=True, null=False)
    tags = models.TextField(blank=True, null=False)
    location = models.CharField(max_length=255, null=False)
    responsibilities = models.TextField(blank=True, null=False)
    compensation = models.CharField(max_length=255, null=False)



#Applicant model
class Applicant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=255, null=False)
    degree = models.CharField(max_length=255, null=False)
    univ = models.CharField(max_length=255, null=False)
    class_name = models.CharField(max_length=255, null=False)
    gpa = models.FloatField(null=False)
    phone = models.IntegerField(null=False)
    email = models.EmailField(null=False)
    photo_url = models.URLField(blank=True, null=False)
    experiences = models.TextField(blank=True, null=False)
    skills = models.TextField(blank=True, null=False)
    docs = models.TextField(blank=True, null=False)
    projects = models.TextField(blank=True, null=False)
    accomplishments = models.TextField(blank=True, null=False)
    affiliations = models.TextField(blank=True, null=False)
    video_url = models.URLField(blank=True, null=False)
    resume_url = models.URLField(blank=True, null=False)
    portfolio_website = models.URLField(blank=True, null=False)
    interest_note = models.TextField(blank=True, null=False)


#Application model
class Application(models.Model):
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE, null=False)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)
    status = models.CharField(max_length=255, choices=job_status.choices, default=job_status.PENDING, null=False)
    p1a = models.TextField(blank=True, null=False)
    p2a = models.TextField(blank=True, null=False)
    p3a = models.TextField(blank=True, null=False)
    p4a = models.TextField(blank=True, null=False)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['applicant', 'job'], name='unique_application')
        ]



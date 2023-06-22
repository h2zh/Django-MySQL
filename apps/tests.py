from django.test import TestCase
from django.utils import timezone
from apps.models import User, Employer, Job, Applicant, Application, user_type, job_status


class ModelTestCase(TestCase):
    def setUp(self):
        # 创建相关的数据文件
        user1 = User.objects.create(email='user1@example.com', password='password1', type=user_type.JOB_SEEKER, created_at=timezone.now())
        user2 = User.objects.create(email='user2@example.com', password='password2', type=user_type.RECRUITER, created_at=timezone.now())
        self.employer1 = Employer.objects.create(name='ABC Inc.',employer=user1)
        self.employer2 = Employer.objects.create(name='XYZ Inc.',employer=user2)
        self.job1 = Job.objects.create(employer=self.employer1, job_title='Software Developer', description='This is a job for a software developer', location='San Francisco Bay Area', compensation='100k - 150k USD per year')
        self.job2 = Job.objects.create(employer=self.employer2, job_title='Marketing Specialist', description='This is a job for a marketing specialist', location='New York City', compensation='80k - 120k USD per year')
        self.applicant1 = Applicant.objects.create(user=user1,name='John Doe', degree='Bachelor\'s', class_name='2022', gpa=3.5, phone=1234567890, email='john.doe@example.com', experiences='Internship at ABC Inc.', skills='Python, Java', accomplishments='Won first prize in coding competition', affiliations='Member of ACM, IEEE')
        self.application1 = Application.objects.create(applicant=self.applicant1, job=self.job1)
        self.application2 = Application.objects.create(applicant=self.applicant1, job=self.job2, status=job_status.INTERVIEWED)

    def test_users_creation(self):
        user1 = User.objects.get(email='user1@example.com')
        user2 = User.objects.get(email='user2@example.com')
        self.assertEqual(user1.password, 'password1')
        self.assertEqual(user2.type, user_type.RECRUITER)

    def test_employers_creation(self):
        employer1 = Employer.objects.get(name='ABC Inc.')
        user1 = User.objects.get(email='user1@example.com')
        self.assertEqual(employer1.employer, user1)

    def test_jobs_creation(self):
        job1 = Job.objects.get(employer=self.employer1)
        job2 = Job.objects.get(employer=self.employer2)
        self.assertEqual(job1.description, 'This is a job for a software developer')
        self.assertEqual(job2.location, 'New York City')

    def test_applicants_creation(self):
        applicant1 = Applicant.objects.get(name='John Doe')
        self.assertEqual(applicant1.gpa, 3.5)

    def test_applications_creation(self):
        application1 = Application.objects.get(applicant=self.applicant1, job=self.job1)
        application2 = Application.objects.get(applicant=self.applicant1, job=self.job2)
        self.assertEqual(application1.status, job_status.PENDING)
        self.assertEqual(application2.status, job_status.INTERVIEWED)
# A Django project with MySQL

## Getting Started

First, create your virtual environment for Django (if you already got one, skip this step)

```bash
python -m venv /path/to/new/virtual/environment
```

Second, change directory to this project, enter the virtual environment you just set up, and install all the packages

```bash
cd path/to/this/project
source </path/to/new/virtual/environment>/bin/activate
(<env_name>)$ pip install -r requirements.txt
```

Third, create a new empty database named `django_learn` on your local MySQL GUI. 
Here is how to do it on [MySQL Workbench](https://stackoverflow.com/a/22164216).
Then, configure the MySQL connection in `django_model/settings.py`, line 87-91.

Now you can migrate the database schema from `apps/models.py` to your local MySQL database
by running

```bash
python manage.py makemigrations
python manage.py migrate
```

You can also run some unit tests in `apps/tests.py` by running

```bash
python manage.py test
```

Lastly, if you want to write some sample data into the database and check them in MySQL Workbench,
you can run

```bash
python manage.py shell
```

Then paste the following code snippet to the terminal and hit enter. Now you should see some sample
data entries in the MySQL Workbench

```bash
from apps.models import User, Employer, Job, Applicant, Application,user_type,job_status
from django.utils import timezone

user1 = User.objects.create(email='user1@example.com', password='password1', type=user_type.JOB_SEEKER, created_at=timezone.now())
user2 = User.objects.create(email='user2@example.com', password='password2', type=user_type.RECRUITER, created_at=timezone.now())
employer1 = Employer.objects.create(name='ABC Inc.',employer=user1)
employer2 = Employer.objects.create(name='XYZ Inc.',employer=user2)
job1 = Job.objects.create(employer=employer1, job_title='Software Developer', description='This is a job for a software developer', location='San Francisco Bay Area', compensation='100k - 150k USD per year')
job2 = Job.objects.create(employer=employer2, job_title='Marketing Specialist', description='This is a job for a marketing specialist', location='New York City', compensation='80k - 120k USD per year')
applicant1 = Applicant.objects.create(user=user1, name='John Doe', degree="Bachelor's", class_name='2022', gpa=3.5, phone='1234567890', email='john.doe@example.com', experiences='Internship at ABC Inc.', skills='Python, Java', accomplishments='Won first prize in coding competition', affiliations='Member of ACM, IEEE')
application1 = Application.objects.create(applicant=applicant1, job=job1)
application2 = Application.objects.create(applicant=applicant1, job=job2, status=job_status.INTERVIEWED)
```
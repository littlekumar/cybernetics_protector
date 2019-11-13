from django.db import models

# Create your models here.
from django.db import models

class adminlogin(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=50)

class success_stories(models.Model):
    title = models.CharField(max_length=30)
    Description = models.CharField(max_length=100)

class Job_Postings(models.Model):
    Job = models.CharField(max_length=30,default=False,primary_key=True)
    Title = models.CharField(max_length=30)
    Qualification = models.CharField(max_length=50)
    Percentage = models.IntegerField()
    Experience = models.IntegerField(help_text="In Years")
    Last_date = models.DateField()
    Location = models.CharField(max_length=100)
    Salary = models.DecimalField(max_digits=10,decimal_places=2)

class CreateAgent(models.Model):
    Agent_id=models.CharField(unique=True,max_length=10)
    Agent_Name = models.CharField(max_length=30)
    Password =models.CharField(max_length=50)
    Dob = models.DateField()
    Contact_Number = models.IntegerField()
    Qualification = models.CharField(max_length=30)
    Address	= models.CharField(max_length=100)

    def __str__(self):
        return self.Agent_id

class Tips(models.Model):
    Name = models.CharField(max_length=30)
    Location = models.CharField(max_length=50)
    Suggession = models.CharField(max_length=100)

class Applicants(models.Model):
    JOB_TITLE = models.CharField(max_length=10,default=False)
    Full_Name = models.CharField(max_length=30)
    Dob = models.DateField()
    Qualification = models.CharField(max_length=30)
    percentage = models.IntegerField()
    Experience = models.IntegerField()
    Contact_Number = models.IntegerField()


# class CaseDetails(models.Model):
#     agent_id = models.IntegerField()
#     case_id = models.IntegerField()
#     case_name= models.CharField(max_length=30)
#     evidence= models.CharField(max_length=30)
#     status= models.CharField(max_length=30)

class Defence_Login(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=50)

class CaseCreation(models.Model):
    case_id=models.CharField(unique=True,max_length=10)
    case_name = models.CharField(max_length=30)
    case_details = models.CharField(max_length=30)
    doc = models.DateField()
    evidence = models.CharField(max_length=30)
    evidence_img=models.FileField(upload_to='evidence_imgs/',default=False)
    Agent_id=models.IntegerField(default=False)
    def __str__(self):
        return self.case_id

class Assign_Agent(models.Model):
    agent_id = models.ManyToManyField(CreateAgent)
    case_id = models.ManyToManyField(CaseCreation)
    description=models.CharField(max_length=50)
#

class CaseAssign_Agent(models.Model):
    agent_id = models.ManyToManyField(CreateAgent)
    case_id = models.ManyToManyField(CaseCreation)
    description=models.CharField(max_length=50)
class Min_admin(models.Model):
    uname=models.CharField(max_length=30)
    upass=models.CharField(max_length=30)
class CaseStatus(models.Model):
    case_id=models.IntegerField()
    Agent_id=models.IntegerField()
    cstatus=models.CharField(max_length=20)
    other_evidence=models.FileField(upload_to='other_images/')

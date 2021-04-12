from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=100)
    objective = models.CharField(max_length=200, blank=True)
    address = models.CharField(max_length=200)
    phoneno = models.CharField(max_length=12)
    email = models.EmailField(max_length=100)
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    university = models.CharField(max_length=100, blank=True)
    degree = models.CharField(max_length=50, blank=True)
    stream = models.CharField(max_length=100, blank=True)
    currentYear = models.CharField(max_length=5, blank=True)
    univStartingYear = models.CharField(max_length=20, blank=True)
    univPassingYear = models.CharField(max_length=20, blank=True)
    univResult = models.CharField(max_length=5, blank=True)
    intermediateSchool = models.CharField(max_length=100, blank=True)
    intermediateSubjects = models.CharField(max_length=100, blank=True)
    intermediateStartingYear = models.CharField(max_length=20, blank=True)
    intermediatePassingYear = models.CharField(max_length=20, blank=True)
    intermediateMarks = models.CharField(max_length=15, blank=True)
    highSchool = models.CharField(max_length=100, blank=True)
    highSchoolSubjects = models.CharField(max_length=100, blank=True)
    highSchoolStartingYear = models.CharField(max_length=20, blank=True)
    highSchoolPassingYear = models.CharField(max_length=20, blank=True)
    highSchoolMarks = models.CharField(max_length=15, blank=True)
    jobTitle = models.CharField(max_length=100, blank=True)
    jobStartDate = models.CharField(max_length=20, blank=True)
    jobEndDate = models.CharField(max_length=20, blank=True)
    jobDescription = models.CharField(max_length=100, blank=True)
    projectTitle = models.CharField(max_length=100, blank=True)
    projectStartDate = models.CharField(max_length=20, blank=True)
    projectEndDate = models.CharField(max_length=20, blank=True)
    projectDescription = models.CharField(max_length=100, blank=True)
    skillDetail = models.CharField(max_length=200)
    languageDetail = models.CharField(max_length=200)
    areaOfInterest = models.CharField(max_length=100, blank=True)
    extracurricularDetail = models.CharField(max_length=100, blank=True)    

class Contact(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField()
    phoneno = models.CharField(max_length=12)
    msg = models.TextField()

    def __str__(self):
        return self.name

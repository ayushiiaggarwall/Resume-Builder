from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Profile, Contact
from django.core.mail import send_mail
from django.conf import settings
from django.core import mail
from django.core.mail.message import EmailMessage
from django.http import HttpResponse
from django.template import loader, Context
from django.template.loader import get_template
from django.views import View
import io as StringIO
from io import StringIO, BytesIO
import urllib
import urllib.request
from bs4 import BeautifulSoup
import csv
import os
from xhtml2pdf import pisa
from reportlab.platypus.doctemplate import SimpleDocTemplate, Spacer
from reportlab.platypus.paragraph import Paragraph
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from django.views.generic import View
import pdfkit

# Create your views here.

def index(request):

    if request.method == "POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        phoneno=request.POST.get("phoneno")
        msg=request.POST.get("msg")
        
        myquery = Contact(name=name, email=email, phoneno=phoneno, msg=msg)
        myquery.save()

#Sending Email
        from_email = settings.EMAIL_HOST_USER
        connection = mail.get_connection()
        connection.open()
        email_message = mail.EmailMessage(f'Email From {name}', f'User Email : {email}\n User Phone Number:{phoneno}\n Message from User: {msg}', from_email, ['aggarwalayushi0306@gmail.com'], connection=connection)

        email_message_user = mail.EmailMessage(f'ResumeBuilder Response', f'Hey {name}\n\n Thanks for reaching us.\n We will get back to you soon.', from_email, [email], connection=connection)

        connection.send_messages([email_message, email_message_user])
        connection.close()
        
        messages.info(request, "Your response has been recorded. Thanks for reaching us.")
        return redirect('/#home')


    return render(request, 'index.html')


def signupPage(request):

    if request.method == "POST":
        uname=request.POST.get("Username")
        fname=request.POST.get("Fname")
        lname=request.POST.get("Lname")
        email=request.POST.get("Emailid")
        pass1=request.POST.get("Password")
        pass2=request.POST.get("confirmPassword")

        if pass1 != pass2:
            messages.error(request, "Password doesn't match!")
            return redirect('/signup')

        try:
            if User.objects.get(username = uname):
                messages.warning(request, "Username is already taken!")
                return redirect('/signup')

        except Exception as identifier:
            pass

        try:
            if User.objects.get(email = email):
                messages.warning(request, "Email ID is already registered!")
                return redirect('/signup')

        except Exception as identifier:
            pass

        myuser = User.objects.create_user(uname, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()

        messages.success(request, "SignUp Successful!")
        return redirect('/login')

    return render(request, 'signup.html')

def loginPage(request):

    if request.method == "POST":
        uname=request.POST.get("Username")
        password=request.POST.get("Password")

        myuser = authenticate(username=uname, password=password)

        if myuser is not None:
            login(request, myuser)
            messages.success(request, "Login Successful!")
            return redirect('/')

        else:
            messages.error(request, "Invalid Credentials!")
            return redirect('/login')

    return render(request, 'login.html')
    

def addResume(request):
    if request.method == "POST":
        name =request.POST.get("name") 
        objective =request.POST.get("objective") 
        address =request.POST.get("address") 
        phoneno =request.POST.get("phoneno") 
        email =request.POST.get("email") 
        github =request.POST.get("github")
        linkedin =request.POST.get("linkedin") 
        university =request.POST.get("university") 
        degree =request.POST.get("degree") 
        stream =request.POST.get("stream") 
        currentYear =request.POST.get("currentYear") 
        univStartingYear =request.POST.get("univStartingYear") 
        univPassingYear =request.POST.get("univPassingYear") 
        univResult =request.POST.get("univResult")
        intermediateSchool =request.POST.get("intermediateSchool") 
        intermediateSubjects =request.POST.get("intermediateSubjects") 
        intermediateStartingYear =request.POST.get("intermediateStartingYear") 
        intermediatePassingYear =request.POST.get("intermediatePassingYear") 
        intermediateMarks =request.POST.get("intermediateMarks") 
        highSchool =request.POST.get("highSchool") 
        highSchoolSubjects =request.POST.get("highSchoolSubjects") 
        highSchoolStartingYear =request.POST.get("highSchoolStartingYear") 
        highSchoolPassingYear =request.POST.get("highSchoolPassingYear") 
        highSchoolMarks =request.POST.get("highSchoolMarks") 
        jobTitle =request.POST.get("jobTitle") 
        jobStartDate =request.POST.get("jobStartDate") 
        jobEndDate =request.POST.get("jobEndDate") 
        jobDescription =request.POST.get("jobDescription") 
        projectTitle =request.POST.get("projectTitle") 
        projectStartDate =request.POST.get("projectStartDate") 
        projectEndDate =request.POST.get("projectEndDate") 
        projectDescription =request.POST.get("projectDescription") 
        skillDetail =request.POST.get("skillDetail") 
        languageDetail =request.POST.get("languageDetail") 
        areaOfInterest =request.POST.get("areaOfInterest") 
        extracurricularDetail =request.POST.get("extracurricularDetail") 

        profile = Profile (name=name, objective=objective, address=address, phoneno=phoneno, email=email, github=github, linkedin=linkedin, university=university, degree=degree, stream=stream, currentYear=currentYear, univStartingYear=univStartingYear, univPassingYear=univPassingYear, univResult=univResult, intermediateSchool=intermediateSchool, intermediateSubjects=intermediateSubjects, intermediateStartingYear=intermediateStartingYear, intermediatePassingYear=intermediatePassingYear, highSchool=highSchool, highSchoolSubjects=highSchoolSubjects, highSchoolStartingYear=highSchoolStartingYear, highSchoolPassingYear=highSchoolPassingYear, highSchoolMarks=highSchoolMarks, jobTitle=jobTitle, jobStartDate=jobStartDate, jobEndDate=jobEndDate, jobDescription=jobDescription, projectTitle=projectTitle, projectStartDate=projectStartDate, projectEndDate=projectEndDate, projectDescription=projectDescription,skillDetail=skillDetail, languageDetail=languageDetail, areaOfInterest=areaOfInterest, extracurricularDetail=extracurricularDetail)
        profile.save()

    return render(request, 'addResume.html' )   


def viewResume(request, id):
    user_profile = Profile.objects.get(pk=id)
    # template = loader.get_template(viewResume)

    return render(request, "viewResume.html", {'user_profile':user_profile})
   

def listResume(request):
    profile=Profile.objects.all()
    return render(request, "listResume.html", {'profile':profile})


def logoutPage(request):
    logout(request)
    messages.success(request, 'Logout Successful!')
    return redirect('/login')
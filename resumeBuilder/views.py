from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Profile, Contact
from django.core.mail import send_mail
from django.conf import settings
from django.core import mail
from django.core.mail.message import EmailMessage
from django.views import View
import csv
import os
from django.views.generic import View
from django.forms.models import model_to_dict


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
        email_message = mail.EmailMessage(f'Email From {name}', f'User Email : {email}\n User Phone Number:{phoneno}\n Message from User: {msg}', from_email, ['ayuresumebuilder@gmail.com'], connection=connection)

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
        userid = request.POST.get("userid")
        name =request.POST.get("name") 
        objective =request.POST.get("objective") 
        address =request.POST.get("address") 
        phoneno =request.POST.get("phoneno") 
        email =request.POST.get("email") 
        github =request.POST.get("github")
        linkedin =request.POST.get("linkedin") 
        university1 =request.POST.get("university1") 
        degree1 =request.POST.get("degree1") 
        stream1 =request.POST.get("stream1") 
        currentYear1 =request.POST.get("currentYear1") 
        univStartingYear1 =request.POST.get("univStartingYear1") 
        univPassingYear1 =request.POST.get("univPassingYear1") 
        univResult1 =request.POST.get("univResult1")
        university2 =request.POST.get("university2") 
        degree2 =request.POST.get("degree2") 
        stream2 =request.POST.get("stream2") 
        currentYear2 =request.POST.get("currentYear2") 
        univStartingYear2 =request.POST.get("univStartingYear2") 
        univPassingYear2 =request.POST.get("univPassingYear2") 
        univResult2 =request.POST.get("univResult2")
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
        jobTitle1 =request.POST.get("jobTitle1") 
        jobStartDate1 =request.POST.get("jobStartDate1") 
        jobEndDate1 =request.POST.get("jobEndDate1") 
        jobDescription1 =request.POST.get("jobDescription1") 
        jobTitle2 =request.POST.get("jobTitle2") 
        jobStartDate2 =request.POST.get("jobStartDate2") 
        jobEndDate2 =request.POST.get("jobEndDate2") 
        jobDescription2 =request.POST.get("jobDescription2") 
        jobTitle3 =request.POST.get("jobTitle3") 
        jobStartDate3 =request.POST.get("jobStartDate3") 
        jobEndDate3 =request.POST.get("jobEndDate3") 
        jobDescription3 =request.POST.get("jobDescription3") 
        jobTitle4 =request.POST.get("jobTitle4") 
        jobStartDate4 =request.POST.get("jobStartDate4") 
        jobEndDate4 =request.POST.get("jobEndDate4") 
        jobDescription4 =request.POST.get("jobDescription4") 
        jobTitle5 =request.POST.get("jobTitle5") 
        jobStartDate5 =request.POST.get("jobStartDate5") 
        jobEndDate5 =request.POST.get("jobEndDate5") 
        jobDescription5 =request.POST.get("jobDescription5") 
        projectTitle1 =request.POST.get("projectTitle1") 
        projectStartDate1 =request.POST.get("projectStartDate1") 
        projectEndDate1 =request.POST.get("projectEndDate1") 
        projectDescription1 =request.POST.get("projectDescription1") 
        projectTitle2 =request.POST.get("projectTitle2") 
        projectStartDate2 =request.POST.get("projectStartDate2") 
        projectEndDate2 =request.POST.get("projectEndDate2") 
        projectDescription2 =request.POST.get("projectDescription2") 
        projectTitle3 =request.POST.get("projectTitle3") 
        projectStartDate3 =request.POST.get("projectStartDate3") 
        projectEndDate3 =request.POST.get("projectEndDate3") 
        projectDescription3 =request.POST.get("projectDescription3") 
        projectTitle4 =request.POST.get("projectTitle4") 
        projectStartDate4 =request.POST.get("projectStartDate4") 
        projectEndDate4 =request.POST.get("projectEndDate4") 
        projectDescription4 =request.POST.get("projectDescription4") 
        projectTitle5 =request.POST.get("projectTitle5") 
        projectStartDate5 =request.POST.get("projectStartDate5") 
        projectEndDate5 =request.POST.get("projectEndDate5") 
        projectDescription5 =request.POST.get("projectDescription5") 
        skillDetail =request.POST.get("skillDetail") 
        languageDetail =request.POST.get("languageDetail") 
        areaOfInterest =request.POST.get("areaOfInterest") 
        extracurricularDetail =request.POST.get("extracurricularDetail") 

        profile = Profile (userid=userid, name=name, objective=objective, address=address, phoneno=phoneno, email=email, github=github, linkedin=linkedin, university1=university1, degree1=degree1, stream1=stream1, currentYear1=currentYear1, univStartingYear1=univStartingYear1, univPassingYear1=univPassingYear1, univResult1=univResult1, university2=university2, degree2=degree2, stream2=stream2, currentYear2=currentYear2, univStartingYear2=univStartingYear2, univPassingYear2=univPassingYear2, univResult2=univResult2, intermediateSchool=intermediateSchool, intermediateSubjects=intermediateSubjects, intermediateStartingYear=intermediateStartingYear, intermediatePassingYear=intermediatePassingYear, highSchool=highSchool, highSchoolSubjects=highSchoolSubjects, highSchoolStartingYear=highSchoolStartingYear, highSchoolPassingYear=highSchoolPassingYear, highSchoolMarks=highSchoolMarks, jobTitle1=jobTitle1, jobStartDate1=jobStartDate1, jobEndDate1=jobEndDate1, jobDescription1=jobDescription1, jobTitle2=jobTitle2, jobStartDate2=jobStartDate2, jobEndDate2=jobEndDate2, jobDescription2=jobDescription2, jobTitle3=jobTitle3, jobStartDate3=jobStartDate3, jobEndDate3=jobEndDate3, jobDescription3=jobDescription3, jobTitle4=jobTitle4, jobStartDate4=jobStartDate4, jobEndDate4=jobEndDate4, jobDescription4=jobDescription4, jobTitle5=jobTitle5, jobStartDate5=jobStartDate5, jobEndDate5=jobEndDate5, jobDescription5=jobDescription5, projectTitle1=projectTitle1, projectStartDate1=projectStartDate1, projectEndDate1=projectEndDate1, projectDescription1=projectDescription1, projectTitle2=projectTitle2, projectStartDate2=projectStartDate2, projectEndDate2=projectEndDate2, projectDescription2=projectDescription2, projectTitle3=projectTitle3, projectStartDate3=projectStartDate3, projectEndDate3=projectEndDate3, projectDescription3=projectDescription3, projectTitle4=projectTitle4, projectStartDate4=projectStartDate4, projectEndDate4=projectEndDate4, projectDescription4=projectDescription4, projectTitle5=projectTitle5, projectStartDate5=projectStartDate5, projectEndDate5=projectEndDate5, projectDescription5=projectDescription5, skillDetail=skillDetail, languageDetail=languageDetail, areaOfInterest=areaOfInterest, extracurricularDetail=extracurricularDetail)
        profile.save()

        messages.success(request, "Your resume has been successfully added!")
        return redirect('/addResume')

    return render(request, 'addResume.html')   


def viewResume(request, id):
    user_profile = Profile.objects.get(pk=id)
    return render(request, "viewResume.html", {'user_profile':user_profile})
   

def listResume(request):
    current_user = request.user.username
    userid = Profile.userid

    if Profile.objects.filter(userid = current_user).exists():
        profile=Profile.objects.filter(userid = current_user)
        return render(request, "listResume.html", {'profile':profile})
        
    return render(request, "listResume.html")


def logoutPage(request):
    logout(request)
    messages.success(request, 'Logout Successful!')
    return redirect('/login')
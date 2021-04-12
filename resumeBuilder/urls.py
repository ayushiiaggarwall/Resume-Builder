from django.urls import path
from resumeBuilder import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signupPage, name='signupPage'),
    path('login', views.loginPage, name='loginPage'),
    path('logout', views.logoutPage, name='logoutPage'),
    path('viewResume', views.viewResume, name='viewResume'),
    path('addResume', views.addResume, name='addResume'),
    path('listResume', views.listResume, name='listResume'),
]
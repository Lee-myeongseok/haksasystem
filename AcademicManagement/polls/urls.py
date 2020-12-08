from django.urls import path
from polls import views

app_name = 'polls'

urlpatterns = [
    path('', views.loginpage, name="loginpage"),
    path('newpro/', views.newpro, name="newpro"),
    path('findidpw/', views.findidpw, name="findidpw"),
    path('studentInfo/', views.studentInfo, name="studentInfo"),
    path('subjectlookup/', views.subjectLookUp, name="subjectLookUp"),
    path('choose/', views.subjectChoose, name="subjectChoose"),
    path('logout/', views.logout, name="logout"),
]

from django.urls import path
from polls import views
from .views import LoginView, StudentinfoView, SubjectLookUpView, SubjectChooseView, LogoutView
from .views import NewproView, FindidpwView, Schedule

from .views import NewLoginView, FindUserInfo, UserInfo, AddProfessor
from .views import StudentInfo, ScheduleInfo, GradeInfo, SubjectInfo, SubjectRequest, ChangePwStudent, InfoReqeustStudent
from django.views.decorators.csrf import csrf_exempt

app_name = 'polls'

urlpatterns = [
    path('', LoginView.as_view(), name="loginpage"),
    path('newpro/', NewproView.as_view(), name="newpro"),
    path('findidpw/', FindidpwView.as_view(), name="findidpw"),
    path('studentinfopage/', StudentinfoView.as_view(), name="studentInfo"),
    path('schedule/', Schedule.as_view(), name="schedule"),
    path('subjectlookup/', SubjectLookUpView.as_view(), name="subjectLookUp"),
    path('choose/', SubjectChooseView.as_view(), name="subjectChoose"),
    path('logout/', LogoutView.as_view(), name="logout"),

    path('login/', NewLoginView.as_view(), name="login"),
    path('finduserinfo/', FindUserInfo.as_view(), name="finduserinfo"),
    path('userinfo/', UserInfo.as_view(), name="userinfo"),
    path('addprofessor/', AddProfessor.as_view(), name="addprofessor"),

    path('studentinfo/', StudentInfo.as_view(), name="studentinfo"),
    path('scheduleinfo/', ScheduleInfo.as_view(), name="scheduleinfo"),
    path('gradeinfo/', GradeInfo.as_view(), name="gradeinfo"),
    path('subjectinfo/', SubjectInfo.as_view(), name="subjectinfo"),
    path('subjectrequest/', SubjectRequest.as_view(), name="subjectrequest"),
    path('changepw_s/', ChangePwStudent.as_view(), name="changepw_s"),
    path('inforequest_s/', InfoReqeustStudent.as_view(), name="inforequest_s"),
]

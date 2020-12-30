from django.urls import path
from polls import views
from .views import LoginView, StudentinfoView, SubjectLookUpView, SubjectChooseView, LogoutView
from .views import NewproView, FindidpwView
from django.views.decorators.csrf import csrf_exempt

app_name = 'polls'

urlpatterns = [
    path('', LoginView.as_view(), name="loginpage"),
    path('newpro/', NewproView.as_view(), name="newpro"),
    path('findidpw/', FindidpwView.as_view(), name="findidpw"),
    path('studentInfo/', StudentinfoView.as_view(), name="studentInfo"),
    path('subjectlookup/', SubjectLookUpView.as_view(), name="subjectLookUp"),
    path('choose/', SubjectChooseView.as_view(), name="subjectChoose"),
    path('logout/', LogoutView.as_view(), name="logout"),
]

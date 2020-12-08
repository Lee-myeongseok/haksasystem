from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from polls.models import Logintbl, Studentinfotbl
from polls.models import Fixmajorsubjecttbl, Fixculturesubjecttbl
from polls.models import Majorsubjecttbl, Culturesubjecttbl
from polls.models import Departmenttbl
import json


def loginpage(request):

    if request.method == "GET":
        return render(request, 'polls/loginpage.html')
    elif request.method == "POST":
        username = request.POST.get('userSanbun', None)
        userpw = request.POST.get('passwd', None)

        alluser = Logintbl.objects.all()
        flag = False

        if not (username and userpw):
            return HttpResponseRedirect(reverse('polls:loginpage'))
        else:
            for userid in alluser:
                if userid.id == username:
                    loginuser = userid
                    flag = True
                    break
            if not flag:
                return HttpResponseRedirect(reverse('polls:loginpage'))
            if loginuser.password == userpw:
                request.session['user'] = loginuser.id
                return redirect('studentInfo/')
            else:
                return HttpResponseRedirect(reverse('polls:loginpage'))

        return render(request, 'polls/login.html')


def newpro(request):
    return render(request, 'polls/newPro.html')


def findidpw(request):
    return render(request, 'polls/findIdPw.html')


def studentInfo(request):
    user = request.session['user']
    students = Studentinfotbl.objects.get(student=user)
    return render(request, 'polls/studentInformation.html', {'students': students})


@csrf_exempt
def subjectLookUp(request):
    loginuser = request.session['user']
    user = get_object_or_404(Logintbl, pk=loginuser)
    fixmajorsubjects = Fixmajorsubjecttbl.objects.all()
    fixculturesubjects = Fixculturesubjecttbl.objects.all()
    majorsubjects = Majorsubjecttbl.objects.all()
    culturesubjects = Culturesubjecttbl.objects.all()
    department = Departmenttbl.objects.all()
    return render(request, 'polls/subjectLookUp.html', {'user': user, 'fixmajorsubjects': fixmajorsubjects, 'fixculturesubjects': fixculturesubjects,
                                                        'majorsubjects': majorsubjects, 'culturesubjects': culturesubjects, 'department': department})


@csrf_exempt
def subjectChoose(request):
    loginuser = request.session['user']
    user = get_object_or_404(Logintbl, pk=loginuser)
    if request.method == "POST":
        userdata = json.loads(request.body)
    return render(request, 'polls/subjectChoose.html', {'user': user, 'userdata': userdata})


def logout(request):
    request.session.pop('user')
    return HttpResponseRedirect(reverse('polls:loginpage'))
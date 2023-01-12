from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View, TemplateView

from polls.models import Logintbl, Studentinfotbl
from polls.models import Fixmajorsubjecttbl, Fixculturesubjecttbl
from polls.models import Majorsubjecttbl, Culturesubjecttbl
from polls.models import Departmenttbl
from polls.models import Subjectgroup1Tbl, Subjectgroup2Tbl
from polls.models import Basket1Tbl, Basket2Tbl
from polls.models import Score1Tbl, Score2Tbl
import json


class LoginView(View):
    template_name = 'polls/loginpage.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
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

        return render(request, self.template_name)


class NewproView(TemplateView):
    template_name = 'polls/newPro.html'


class FindidpwView(TemplateView):
    template_name = 'polls/findIdPw.html'


class StudentinfoView(View):
    template_name = 'polls/studentInformation.html'

    def get(self, request, *args, **kwargs):
        user = request.session['user']
        students = Studentinfotbl.objects.get(student=user)
        return render(request, self.template_name, {'students': students})


class Schedule(View):
    template_name = 'polls/schedule.html'

    def get(self, request, *args, **kwargs):
        loginuser = request.session['user']

        context = {'loginuser': loginuser}

        return render(request, self.template_name, context=context)


@method_decorator(csrf_exempt, name='dispatch')
class SubjectLookUpView(View):
    template_name = 'polls/subjectLookUp.html'

    def get(self, request, *args, **kwargs):
        loginuser = request.session['user']
        user = get_object_or_404(Logintbl, pk=loginuser)
        fixmajorsubjects = Fixmajorsubjecttbl.objects.all()
        fixculturesubjects = Fixculturesubjecttbl.objects.all()
        majorsubjects = Majorsubjecttbl.objects.all()
        culturesubjects = Culturesubjecttbl.objects.all()
        department = Departmenttbl.objects.all()
        context = {'user': user, 'fixmajorsubjects': fixmajorsubjects, 'fixculturesubjects': fixculturesubjects,
                   'majorsubjects': majorsubjects, 'culturesubjects': culturesubjects, 'department': department}

        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        userdata = json.loads(request.body)

        loginuser = request.session['user']
        user = get_object_or_404(Logintbl, pk=loginuser)

        if loginuser == '2015032094':
            if Basket1Tbl.objects.count() < 8:
                try:
                    Basket1Tbl.objects.get(subject=userdata[2])
                except:
                    basketdata = Basket1Tbl()
                    basketdata.department = userdata[1]
                    basketdata.subject = userdata[2]
                    basketdata.score = userdata[3]
                    basketdata.professor = userdata[4]
                    basketdata.time = userdata[5]
                    basketdata.place = userdata[6]
                    basketdata.nowmember = userdata[7]
                    basketdata.total = userdata[8]
                    basketdata.save()
        elif loginuser == '20032094':
            if Basket2Tbl.objects.count() < 8:
                try:
                    Basket2Tbl.objects.get(subject=userdata[2])
                except:
                    basketdata = Basket2Tbl()
                    basketdata.department = userdata[1]
                    basketdata.subject = userdata[2]
                    basketdata.score = userdata[3]
                    basketdata.professor = userdata[4]
                    basketdata.time = userdata[5]
                    basketdata.place = userdata[6]
                    basketdata.nowmember = userdata[7]
                    basketdata.total = userdata[8]
                    basketdata.save()

        fixmajorsubjects = Fixmajorsubjecttbl.objects.all()
        fixculturesubjects = Fixculturesubjecttbl.objects.all()
        majorsubjects = Majorsubjecttbl.objects.all()
        culturesubjects = Culturesubjecttbl.objects.all()
        department = Departmenttbl.objects.all()

        context = {'user': user, 'fixmajorsubjects': fixmajorsubjects, 'fixculturesubjects': fixculturesubjects,
                   'majorsubjects': majorsubjects, 'culturesubjects': culturesubjects, 'department': department}

        return render(request, self.template_name, context=context)


@method_decorator(csrf_exempt, name='dispatch')
class SubjectChooseView(View):
    template_name = 'polls/subjectChoose.html'

    def get(self, request, *args, **kwargs):
        loginuser = request.session['user']
        user = get_object_or_404(Logintbl, pk=loginuser)

        if loginuser == '2015032094':
            basketsubjects = Basket1Tbl.objects.all()
        elif loginuser == '20032094':
            basketsubjects = Basket2Tbl.objects.all()

        context = {'user': user, 'basketsubjects': basketsubjects}

        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        subjectdata = json.loads(request.body)

        loginuser = request.session['user']
        user = get_object_or_404(Logintbl, pk=loginuser)

        students = Studentinfotbl.objects.get(student=loginuser)

        if loginuser == '2015032094':
            basketsubjects = Basket1Tbl.objects.all()
        elif loginuser == '20032094':
            basketsubjects = Basket2Tbl.objects.all()

        if subjectdata[0] == "-1":
            pass
        elif subjectdata[0] != "":
            if loginuser == '2015032094':
                for subject_name in subjectdata:
                    basketsubject = Basket1Tbl.objects.get(subject=subject_name)
                    basketsubject.delete()
            elif loginuser == '20032094':
                print(subjectdata)
                for subject_name in subjectdata:
                    basketsubject = Basket2Tbl.objects.get(subject=subject_name)
                    basketsubject.delete()
        else:
            try:
                if subjectdata[1] == "":
                    if loginuser == '2015032094':
                        try:
                            Score1Tbl.objects.get(subjectname=subjectdata[3])
                        except:
                            scores = Score1Tbl()
                            scores.yearsemester = "0" + str(students.grade) + "01"
                            if subjectdata[3] == '컴퓨터활용':
                                scores.subjectcode = "10003"
                            elif subjectdata[3] == 'C언어의 기초':
                                scores.subjectcode = '00101'
                            scores.subjectname = subjectdata[3]
                            scores.rating = ""
                            scores.numrating = 0
                            scores.save()

                            if subjectdata[2] == '교양':
                                if subjectdata[3] == '컴퓨터활용':
                                    select_subject = Culturesubjecttbl.objects.get(culturesubjectcode='10003')
                                    select_subject.nowmember += 1
                                    select_subject.save()

                                    basket_subject = Basket1Tbl.objects.get(subject=subjectdata[3])
                                    basket_subject.nowmember += 1
                                    basket_subject.save()
                                    basket_subject2 = Basket2Tbl.objects.get(subject=subjectdata[3])
                                    basket_subject2.nowmember += 1
                                    basket_subject2.save()
                                else:
                                    pass
                            else:
                                if subjectdata[3] == 'C언어의 기초':
                                    select_subject = Majorsubjecttbl.objects.get(majorsubjectcode='00101')
                                    select_subject.nowmember += 1
                                    select_subject.save()

                                    basket_subject = Basket1Tbl.objects.get(subject=subjectdata[3])
                                    basket_subject.nowmember += 1
                                    basket_subject.save()
                                    basket_subject2 = Basket2Tbl.objects.get(subject=subjectdata[3])
                                    basket_subject2.nowmember += 1
                                    basket_subject2.save()
                                else:
                                    pass
                    elif loginuser == '20032094':
                        try:
                            Score2Tbl.objects.get(subjectname=subjectdata[3])
                        except:
                            scores = Score2Tbl()
                            scores.yearsemester = "0" + str(students.grade) + "01"
                            if subjectdata[3] == '컴퓨터활용':
                                scores.subjectcode = "10003"
                            elif subjectdata[3] == 'C언어의 기초':
                                scores.subjectcode = '00101'
                            scores.subjectname = subjectdata[3]
                            scores.rating = ""
                            scores.numrating = 0
                            scores.save()

                            if subjectdata[2] == '교양':
                                if subjectdata[3] == '컴퓨터활용':
                                    select_subject = Culturesubjecttbl.objects.get(culturesubjectcode='10003')
                                    select_subject.nowmember += 1
                                    select_subject.save()

                                    basket_subject = Basket1Tbl.objects.get(subject=subjectdata[3])
                                    basket_subject.nowmember += 1
                                    basket_subject.save()
                                    basket_subject2 = Basket2Tbl.objects.get(subject=subjectdata[3])
                                    basket_subject2.nowmember += 1
                                    basket_subject2.save()
                                else:
                                    pass
                            else:
                                if subjectdata[3] == 'C언어의 기초':
                                    select_subject = Majorsubjecttbl.objects.get(majorsubjectcode='00101')
                                    select_subject.nowmember += 1
                                    select_subject.save()

                                    basket_subject = Basket1Tbl.objects.get(subject=subjectdata[3])
                                    basket_subject.nowmember += 1
                                    basket_subject.save()
                                    basket_subject2 = Basket2Tbl.objects.get(subject=subjectdata[3])
                                    basket_subject2.nowmember += 1
                                    basket_subject2.save()
                                else:
                                    pass

                else:
                    pass

            except IndexError:
                pass

        context = {'user': user, 'basketsubjects': basketsubjects}

        return render(request, self.template_name, context=context)


class LogoutView(View):

    def get(self, request, *args, **kwargs):
        request.session.pop('user')
        return HttpResponseRedirect(reverse('polls:loginpage'))


class NewLoginView(View):
    template_name = 'polls/login.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class FindUserInfo(View):
    template_name = 'polls/finduserinfo.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class UserInfo(View):
    template_name = 'polls/userinfo.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class AddProfessor(View):
    template_name = 'polls/addprofessor.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
# from django.shortcuts import render
#
# # Create your views here.

from django.http import Http404
from django.views import generic
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponse
# from django.template import loader
from django.shortcuts import render
from .models import Dept, Prof,Projects,Teaching,Recognition,Student,Publication,Experience
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login ,logout
from .forms import UserForm

def index(request):

    all_depts= Dept.objects.all()
    # template = loader.get_template('project/index.html')

    # html = ''
    #
    # for dept in all_depts:
    #     url = '/project/' + str(dept.id) + '/'
    #     html += '<a href ="' + url + '">' + dept.Dept_name + ' </a><br>'
    #15th video

    return render(request, 'project/index.html',{'all_depts': all_depts} )

def about(request):

    all_depts= Dept.objects.all()

    return render(request, 'project/about.html',{'all_depts': all_depts} )


def contact(request):

    all_depts= Dept.objects.all()
    all_profs= Prof.objects.all()


    return render(request, 'project/contact.html',{'all_depts': all_depts , 'all_profs': all_profs} )

def detail(request,dept_id):

    all_depts = Dept.objects.all()
    dept = Dept.objects.get(pk=dept_id)

    return render(request, 'project/detail.html', {'dept': dept, 'all_depts': all_depts})

def prof_detail(request,prof_id):

    all_depts = Dept.objects.all()
    all_profs = Prof.objects.all()
    all_teachings = Teaching.objects.all()
    all_publications = Publication.objects.all()
    all_projects = Projects.objects.all()
    all_recognitions = Recognition.objects.all()
    all_students = Student.objects.all()




    prof = Prof.objects.get(pk=prof_id)

    return render(request, 'project/prof_detail.html', {'prof': prof, 'all_depts': all_depts , 'all_profs': all_profs , 'all_projects': all_projects , 'all_teachings' : all_teachings , 'all_publications' : all_publications , 'all_recognitions': all_recognitions , 'all_students' : all_students })

class ProfCreate(CreateView):

    model = Prof
    fields = [ 'Department' , 'Name' , 'Designation' , 'Image' , 'address1' , 'address2' , 'phone_office' , 'phone_residency' ,'email' , 'Room_No' , 'Research_Interests' ]
    success_url = reverse_lazy('index')

class ProfUpdate(CreateView):

    model = Prof
    fields = [ 'Department' , 'Designation' , 'Image' , 'address1' , 'address2' , 'phone_office' , 'phone_residency' ,'email' , 'Room_No' , 'Research_Interests' ]
    success_url = reverse_lazy('teaching-add')


class ProjectsCreate(CreateView):
    model = Projects
    fields = [ 'Funding_agency' , 'Professor' , 'Name' , 'Detail' , 'Start_date' , 'End_date' ]
    success_url = reverse_lazy('projects-add')


class TeachingCreate(CreateView):
    model = Teaching
    fields = [ 'Professor' , 'Name' , 'Detail' , 'Start_date' , 'End_date' ]
    success_url = reverse_lazy('teaching-add')


class RecognitionCreate(CreateView):
    model = Recognition

    fields = [ 'Professor' , 'Name' , 'Detail' , 'Date' ]
    success_url = reverse_lazy('recognition-add')


class StudentCreate(CreateView):
    model = Student

    fields = [ 'Professor' , 'Name' , 'Detail' , 'Start_date' , 'End_date' ]
    success_url = reverse_lazy('student-add')


class PublicationCreate(CreateView):
    model = Publication

    fields = ['Professor', 'Name', 'Detail', 'Date']
    success_url = reverse_lazy('publication-add')


class ExperienceCreate(CreateView):
    model = Experience

    fields = ['Professor', 'Name', 'Detail', 'Start_date' , 'End_date']
    success_url = reverse_lazy('experience-add')


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'project/login.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                prof = Prof.objects.filter(user=request.user)
                return render(request, 'project/prof_update.html', {'prof': prof})
            else:
                return render(request,'project/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'project/login.html', {'error_message': 'Invalid login'})
    return render(request, 'project/login.html')

#
# def register(request):
#     form = UserForm(request.POST or None)
#     if form.is_valid():
#         user = form.save(commit=False)
#         username = form.cleaned_data['username']
#         password = form.cleaned_data['password']
#         user.set_password(password)
#         user.save()
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             if user.is_active:
#                 login(request, user)
#                 albums = Album.objects.filter(user=request.user)
#                 return render(request, 'music/index.html', {'albums': albums})
#     context = {
#         "form": form,
#     }
#     return render(request, 'music/register.html', context)


class UserFormView(View):

    form_class=UserForm
    template_name = 'project/registration_form.html'

    def get(self,request):

        form=self.form_class(None)
        return render(request,self.template_name, { 'form' : form })


    def post(self, request):

        form=self.form_class(request.POST)

        if form.is_valid():

            user=form.save(commit=False)

            username = form.cleaned_data[ 'username' ]
            password = form.cleaned_data[ 'password' ]

            user.set_password(password)
            user.save()

            user = authenticate(username =username , password=password )

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('prof-add')

        return render(request, self.template_name,{'form' : form})




























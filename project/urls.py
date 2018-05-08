from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.index,name='index'),

    url(r'about/$', views.about, name='about'),
    url(r'contact/$', views.contact, name='contact'),

    url(r'^(?P<dept_id>[0-9]+)/$', views.detail, name='detail'),

    url(r'prof(?P<prof_id>[0-9]+)/$', views.prof_detail, name='prof_detail'),

    url(r'profadd/$', views.ProfCreate.as_view(), name='prof-add'),

    url(r'teachingadd/$', views.TeachingCreate.as_view(), name='teaching-add'),
    url(r'projectsadd/$', views.ProjectsCreate.as_view(), name='projects-add'),
    url(r'studentadd/$', views.StudentCreate.as_view(), name='student-add'),
    url(r'recognitionadd/$', views.RecognitionCreate.as_view(), name='recognition-add'),
    url(r'publicationadd/$', views.PublicationCreate.as_view(), name='publication-add'),
    url(r'experienceadd/$', views.ExperienceCreate.as_view(), name='experience-add'),

    url(r'profupdate/$', views.ProfUpdate.as_view(), name='prof-update'),

    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),

]

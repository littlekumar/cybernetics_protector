"""cybernetics_protector URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from app import views
from cybernetics_protector import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', TemplateView.as_view(template_name="home.html"),name='home_page'),
    path('admin_loginpage/',TemplateView.as_view(template_name='admin_loginpage.html'),name='admin_loginpage'),
    path('agent_loginpage/', TemplateView.as_view(template_name='agent_loginpage.html'), name='agent_loginpage'),
    path('minisryofdef_loginpage/', TemplateView.as_view(template_name='ministary_deflogin.html'), name='ministryof_loginpage'),
    path('aboutus/', TemplateView.as_view(template_name="aboutus.html"), name='aboutus_page'),
    path('admin_logincheck/',views.admin_logincheck,name='admin_logincheck'),
    path('agent_logincheck/',views.agent_logincheck,name='agent_logincheck'),
    path('minofdef_logincheck/',views.minofdef_logincheck,name='minofdef_logincheck'),
    path('add_succes_story',TemplateView.as_view(template_name='add_succes_story.html'),name='add_succes_story'),
    path('admin_logout/',views.admin_logout,name='admin_logout'),
    path('job_posting/',TemplateView.as_view(template_name='job_posting.html'),name='job_posting'),
    path('agent_management/',TemplateView.as_view(template_name='agent_management.html'),name='agent_management'),
    path('create_agent/',TemplateView.as_view(template_name='create_agentpage.html'),name='create_agent'),
    path('update_agent/',views.update_agent,name='update_agent'),
    path('view_agent/',views.view_agent,name='view_agent'),
    path('create_case/',TemplateView.as_view(template_name='create_case.html'),name='create_case'),
    path('open_sucess_stories/',TemplateView.as_view(template_name='open_sucess_stories.html'),name='open_sucess_stories'),
    path('story1/',TemplateView.as_view(template_name='story1.html'),name='story1'),
    path('story2/', TemplateView.as_view(template_name='story2.html'), name='story2'),
    path('all_stories/',views.all_stories,name='all_stories'),
    path('save_succes_story/',views.save_succes_story,name='save_succes_story'),
    path('save_job/',views.save_job,name='save_job'),
    path('find_job/',views.find_job,name='find_job'),
    path('save_agent/',views.save_agent,name='save_agent'),
    path('save_case/',views.save_case,name='save_case'),
    path('appointing_agent/',views.appointing_agent,name='appointing_agent'),
    path('apply_job/',views.apply_job,name='apply_job'),
    path('applyjob_save/',views.applyjob_save,name='applyjob_save'),
    path('applyjob_list/',views.applyjob_list,name='applyjob_list'),
    path('agent_details/',views.agent_details,name='agent_details'),
    path('assignto_agent/',views.assignto_agent,name='assignto_agent'),
    path('assigncase_agent/',views.assigncase_agent,name='assigncase_agent'),
    path('agent_casedetails/',views.agent_casedetails,name='agent_casedetails'),
    path('getagent_case_details/',views.getagent_case_details,name='getagent_case_details'),
    path('agent_logout/',views.agent_logout,name='agent_logout'),
    path('delete_agent/',views.delete_agent,name='delete_agent'),
    path('update_agent1/',views.update_agent1,name='update_agent1'),
    path('upas/',views.upas,name='upas'),
    path('upca/',views.upca,name='upca'),
    path('ucsd/',views.ucsd,name='ucsd'),
    path('reports/',views.reports,name='reports')

]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

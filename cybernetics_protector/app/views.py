from django.shortcuts import render, redirect

from .models import success_stories,Job_Postings,CreateAgent,CaseCreation,Applicants,adminlogin,Defence_Login,CaseStatus
from .form import Agent_AsignForm# Create your views here.
def admin_logincheck(request):
    username=request.POST['username']
    password=request.POST['password']
    try:
        res=adminlogin.objects.get(username=username,password=password)
        if res:
            return render(request,'welcome_adminpage.html')
    except:
        return render(request,'admin_loginpage.html',{'msg':"Invalid User_id/Password"})


def agent_logincheck(request):
    username = request.POST['username']
    password = request.POST['password']
    try:
        res=CreateAgent.objects.get(Agent_id=username,Password=password)
        if res:
            return render(request, 'welcome_agrntpage.html',{'data':res.Agent_id})
    except:
        return render(request, 'agent_loginpage.html', {'msg': "Invalid User_id/Password"})


def minofdef_logincheck(request):
    username = request.POST['username']
    password = request.POST['password']
    try:
        res=Defence_Login.objects.get(username=username,password=password)
        if res:
            return render(request, 'welcome_minof_defpage.html')
    except:
        return render(request, 'ministary_deflogin.html', {'msg': "Invalid User_id/Password"})


def admin_logout(request):
    return redirect('admin_loginpage')





def update_agent(request):
    pass


def view_agent(request):
    pass


def all_stories(request):
    data=success_stories.objects.all()
    return render(request,'all_sucess_stories.html',{'data':data})


def save_succes_story(request):
    title=request.POST['title']
    comment=request.POST['comment']
    success_stories(title=title,Description=comment).save()
    return render(request,'add_succes_story.html',{'data':"Story Saved Succesfully"})


def save_job(request):
    job = request.POST['job']
    title=request.POST['title']
    qualification = request.POST['qualification']
    percentage = request.POST['percentage']
    experiance = request.POST['experiance']
    last_date = request.POST['last_date']
    location = request.POST['location']
    salary = request.POST['salary']
    Job_Postings(Job=job,Title=title,Qualification=qualification,Percentage=percentage,Experience=experiance,
                 Last_date=last_date,Location=location,Salary=salary).save()

    return render(request,'job_posting.html',{'msg':"Job Posted Succesfully"})


def find_job(request):
    data=Job_Postings.objects.all()
    return render(request,'find_job.html',{'data':data})


def save_agent(request):
    agent_id=request.POST['agent_id']
    agent_name=request.POST['agent_name']
    dob=request.POST['dob']
    contactno=request.POST['contactno']
    qualification=request.POST['qualification']
    addres=request.POST['addres']
    password=request.POST['password']
    try:
        CreateAgent(Agent_id=agent_id,Agent_Name=agent_name,Dob=dob,Contact_Number=contactno,Qualification=qualification,Address=addres,Password=password).save()
        return render(request, 'create_agentpage.html', {'msg': "Agent Create Succesfully"})
    except:
        a=CreateAgent.objects.values_list('Agent_id')
        l=len(a)
        idno=a[l-1][0]+1
        return render(request, 'create_agentpage.html', {'msg': "Agent Id Alredy Available Please Give"+str(idno)})


def save_case(request):
    caseid=request.POST['caseid']
    case_name=request.POST['case_name']
    case_details=request.POST['case_details']
    doc=request.POST['doc']
    evidence_provided=request.POST['evidence_provided']
    evidence_proof=request.FILES['evidence_proof']
    try:
        CaseCreation(case_id=caseid,case_name=case_name,case_details=case_details,doc=doc,evidence_img=evidence_proof,evidence=evidence_provided).save()
        return render(request,'create_case.html',{'msg':"Case Created Suceessfully"})
    except:
        a = CaseCreation.objects.values_list('case_id')
        l = len(a)
        idno = a[l - 1][0] + 1
        return render(request, 'create_case.html', {'msg': "Case Id Alredy Available Please Give" + str(idno)})

# from .form import CaseAssign_AgentForm
# def appointing_agent(request):
#     fr=CaseAssign_AgentForm
#     return render(request,'appointing_agent.html',{'form':fr})
from .form import CaseAssign_AgentForm
def appointing_agent(request):
    data=CaseCreation.objects.all()
    return render(request,'casedetails.html',{'data':data})


def apply_job(request):
    jobtype=request.GET['jobtype']
    return render(request,'apply_job.html',{'data':jobtype})


def applyjob_save(request):
    jobtype=request.POST['jobtype']
    fullname=request.POST['fullname']
    dob=request.POST['dob']
    qualification=request.POST['qualification']
    percentage=request.POST['percentage']
    experiance=request.POST['experiance']
    contactno=request.POST['contactno']
    Applicants(JOB_TITLE=jobtype,Full_Name=fullname,Dob=dob,
               Qualification=qualification,percentage=percentage,
               Experience=experiance,Contact_Number=contactno).save()
    return render(request,'find_job.html',{'msg':"Appiled Job Succesfully"})


def applyjob_list(request):
    data=Applicants.objects.all()
    return render(request,'applyjob_list.html',{'data':data})


def agent_details(request):
    try:
        res=request.GET['ud']
        data = CreateAgent.objects.all()
        return render(request, 'agent_details.html', {'data': data,'data2':'data2'})
    except:
        data=CreateAgent.objects.all()
        return render(request,'agent_details.html',{'data':data})


def assignto_agent(request):
    caseid=request.GET['caseid']
    res=CreateAgent.objects.all()



    return render(request,'assignto_agent.html',{'caseid':caseid,'data':res})


def assigncase_agent(request):
    caseid=request.POST['caseid']
    agentid=request.POST['agentid']

    res=CaseCreation.objects.get(case_id=caseid)
    res.Agent_id=agentid
    res.save()
    return redirect('appointing_agent')


def agent_casedetails(request):
    agentid=request.GET['id']
    try:
        res = CaseCreation.objects.filter(Agent_id=agentid)
        return render(request, 'agent_casedetails.html', {'data': res})
    except:
        return render(request, 'agent_casedetails.html', {'msg': "No Case Details"})



def getagent_case_details(request):
    pass


def agent_logout(request):
    return render(request,'agent_loginpage.html')


def delete_agent(request):
    id=request.GET['id']
    CreateAgent.objects.get(Agent_id=id).delete()

    return redirect('agent_details')


def update_agent1(request):
    id=request.GET['id']
    data=CreateAgent.objects.get(Agent_id=id)
    return render(request,"upagent.html",{'data':data})


def upas(request):
    agent_id=request.POST['aid']
    agent_name=request.POST['an']
    contactno=request.POST['ac']
    qualification=request.POST['aq']
    addres=request.POST['aa']
    res=CreateAgent.objects.get(Agent_id=agent_id)
    res.Agent_Name=agent_name
    res.Contact_Number=contactno
    res.Qualification=qualification
    res.Address=addres
    res.save()
    return redirect('agent_details')


def upca(request):
    id=request.GET['id']
    res=CaseCreation.objects.filter(Agent_id=id)
    return render(request,'upc.html',{'data':res})


def ucsd(request):
    cid=request.POST['cid']
    aid=request.POST['aid']
    cts=request.POST['cts']
    ote=request.FILES['ote']
    CaseStatus(case_id=cid,Agent_id=aid,cstatus=cts,other_evidence=ote).save()
    res=CaseCreation.objects.filter(Agent_id=aid)
    return render(request,'upc.html',{'data':res,'data2':"Case Update Succesfully"})


def reports(request):
    res=CaseStatus.objects.all()
    return render(request,'reports.html',{'data':res})
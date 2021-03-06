from django.shortcuts import render,redirect
from django.http import HttpResponse
#...
from django.template import loader
import json
import webapp.iof as iof
import os
#from .forms import RegisterForm

def index(request):
    return HttpResponse("Hello, world. You're at the webapp index.")

# Create your views here.

def loginw(request):
	return render(request,'webapp/login.html')
	#return HttpResponse("login.")

def register(request):
	return render(request,'webapp/register.html') 


def CreateAudit(request):
	return render(request,'webapp/CreateAudit.html')


def AuditorList(request):
	l = []
	context = {}
	with open('auditor.txt','r') as f:
		try:
			l = json.load(f)
		except:
			 return HttpResponse("<h1>no Auditors registered yet</h1>")

		context['auditor_list'] = l
	print(context)
	
	return render(request,'webapp/Auditors.html',context)

def DeleteAuditor(request,emp_id):
	context = {}
	context['emp_id'] = emp_id
	iof.del_auditor(emp_id)
	return render(request,'webapp/DeleteAuditor.html',context)



def AuditList(request):
	l = []
	context = {}
	with open('audit.txt','r') as f:
		try:
			l = json.load(f)
		except:
			 return HttpResponse("<h1>no Audits created yet</h1>")

		context['audit_list'] = l
	print(context)
	
	return render(request,'webapp/AuditList.html',context)


def AuditSheets(request,file_id):
	context = {}
	context['audit_id'] = file_id[:4]
	context['file_id'] = file_id
	print(file_id)
	sheets = iof.read_sheet(file_id)
	context['sheet_list'] = sheets
	return render(request,'webapp/AuditSheets.html',context)


def EditAuditor(request,emp_id):
	context = {}
	print(emp_id)
	context['emp_id'] = emp_id
	return render(request,'webapp/edit_auditor.html',context)


def EditAudit(request,audit_id):
	context = iof.auditdetails(audit_id) 
	return render(request,'webapp/EditAudit.html',context)

def CreateSheet(request,file_id):
	context = {}
	context['file_id'] = file_id
	return render(request,'webapp/CreateSheet.html',context)

def questions(request,s_id):
	context = {}
	context['s_id'] = s_id
	question_list = iof.read_questions(s_id)
	context['question_list'] = question_list
	print(question_list)
	return render(request,'webapp/questions.html',context)

def CreateQuestions(request,s_id):
	context = {}
	context['s_id'] = s_id
	return render(request,'webapp/CreateQuestions.html',context)

def CreateFile(request,audit_id):
	context = {}
	context['audit_id'] = audit_id
	return render(request,'webapp/CreateFile.html',context)

def AuditFiles(request,audit_id):
	context = {}
	context['audit_id'] = audit_id
	print(audit_id)
	files = iof.read_file(audit_id)
	context['file_list'] = files
	return render(request,'webapp/AuditFiles.html',context)

def AuditDashboard(request,audit_id):
	context = iof.auditdetails(audit_id)
	l = iof.read_Audits()
	if audit_id in l:
		context['ongoing'] = 1
	else:
		context['ongoing'] = 0
	return render(request,'webapp/AuditDashboard.html',context)


def AdminMenu(request):
	context = {}
	return render(request,'webapp/AdminMenu1.html',context)

def AddAuditor(request,audit_id):
	context ={}
	context['audit_id'] = audit_id
	l =[]
	with open('auditor.txt','r') as f:
		try:
			l = json.load(f)
		except:
			 return HttpResponse("<h1>no Auditors registered yet</h1>")

		context['auditor_list'] = l
	print(context)

	return render(request,'webapp/AddAuditor.html',context)


#######formshandles#############
def get_auditor(request):
	d = {}
	l = []
	context={}
	if request.method == 'POST':
		form = request.POST
		d['email'] = form['email']
		d['f_name'] = form['first_name']
		d['l_name'] = form['last_name']
		d['emp_id'] = form['emp_id']
		if d['emp_id'] in (open('auditor.txt','r').read()):
			context["message"] = 'INVALID EMPLOYEE ID'
			return render(request,'webapp/register.html',context)
		d['password'] = iof.password_generator()
		print(d)

		with open('auditor.txt', 'r+') as f:
			try:
				l = json.load(f)
			except:
				l = []

			l.append(d)
			f.seek(0)
			json.dump(l,f)
			print(l)
		return render(request,'webapp/success_auditor.html',context) 


def get_audit(request):
	context = {}
	if request.method == 'POST':
		form = request.POST
		context['audit_name'] = form['audit_name']
		context['audit_type'] = form['audit_type']
		context['audit_id']   = form['audit_id']
		context['description']  = form['description']
		print(context)
		if context['audit_id'] in (open('audit.txt','r').read()):
			context["message"] = 'INVALID AUDIT ID'
			return render(request,'webapp/CreateAudit.html',context)

		with open('audit.txt', 'r+') as f:
			try:
				l = json.load(f)
			except:
				l = []

			l.append(context)
			f.seek(0)
			json.dump(l,f)
			print(l)
		return render(request,'webapp/success_audit.html',context)

def get_sheet(request,file_id):
	context = {}
	if request.method == 'POST':
		form  = request.POST
		context['file_id'] = file_id
		context['sheet_name'] = form['sheet_name']
		context['s_id'] = file_id+form['sheet_name']
		context['status'] = 0
		if context['s_id'] in (open('sheets.txt','r').read()):
			context["message"] = 'Sheet name Already exists'
			return render(request,'webapp/CreateSheet.html',context)

		with open('sheets.txt', 'r+') as f:
			try:
				l = json.load(f)
			except:
				l = []

			l.append(context)
			f.seek(0)
			json.dump(l,f)
			print(l)
		return render(request,'webapp/success_sheet.html',context)

def get_questions(request,s_id):
	context = {}
	if request.method == 'POST':
		form = request.POST
		context['s_id'] = s_id
		context['q'] = form['q']
		context['q_type'] = form['q_type']

		with open('questions.txt', 'r+') as f:
			try:
				l = json.load(f)
			except:
				l = []

			l.append(context)
			f.seek(0)
			json.dump(l,f)
			print(l)
			
		return render(request,'webapp/success_question.html',context)

def get_file(request,audit_id):
	context = {}
	if request.method == 'POST':
		form  = request.POST
		context['audit_id'] = audit_id
		context['file_name'] = form['file_name']
		context['f_id'] = audit_id+form['file_name']
		if context['f_id'] in (open('files.txt','r').read()):
			context["message"] = 'file name Already exists'
			return render(request,'webapp/CreateFile.html',context)

		with open('files.txt', 'r+') as f:
			try:
				l = json.load(f)
			except:
				l = []

			l.append(context)
			f.seek(0)
			json.dump(l,f)
			print(l)
		return render(request,'webapp/success_file.html',context)

def edit_audit(request,audit_id):
	
	if request.method == 'POST':
		form = request.POST
		context = form
		print(form['username'])
		with open('audit.txt', 'r+') as f:
			l = json.load(f)
			print(l)
			for i in l:
				if i['audit_id'] == audit_id:
					i['audit_name'] = form['audit_name']
					i['audit_type'] = form['audit_type']
					i['description'] = form['description']
			f.truncate()
			f.seek(0)
			json.dump(l,f)
		return render(request,'webapp/success_audit.html',context)

def login_handle(request):
	context = {}
	if request.method == 'POST':
		form = request.POST
		print("form is",form)
		print(form)
		if form['username'] == 'admin' and form['password'] == 'admin':
			return render(request,'webapp/AdminMenu.html')
		else:
			context['msg'] == 'invalid username or password'
			return render(request,'webapp/login.html',context)

def get_auditor_audit(request,audit_id):
	l = []
	d = iof.read_Auditor_Audit()
	context = {}
	context['audit_id'] = audit_id
	if request.method == 'POST':
		form = request.POST
		print(form.getlist('emp_id'))
		d[audit_id] = form.getlist('emp_id')
		print(d)
		iof.write_Auditor_Audit(d)
		
		return render(request,'webapp/success_AuditorAudit.html',context)

def monitor(request,audit_id):
	total = 0
	remaining = 0
	context = {}
	status  = iof.read_status()
	for i in status:
		print(i)
		total = total + i['incomplete']+i['complete']
		remaining = remaining + i['incomplete']

	print(total)
	print(remaining)
	context['complete'] = total - remaining
	context['incomplete'] = remaining
	d = iof.read_Auditor_Audit()
	emp_list = d[audit_id]
	print(str(emp_list))

	graph = []
	for i in emp_list:
		 ele = {}
		 ele['emp_id'] = i
		 files = iof.read_ongoing_files(i)
		 incomplete = 0
		 complete = 0
		 for j in status:
		 	if j['f_id'] in files:
		 		complete = complete + j['complete']
		 		incomplete = incomplete + j['incomplete']
		 ele['complete'] = complete
		 ele['incomplete'] = incomplete
		 graph.append(ele)
		 print(ele)
	context['graph'] = graph
	


	return render(request,'webapp/monitor.html',context)

def auditstart(request,audit_id):
	context = {}
	iof.start_audit(audit_id)
	
	return AuditDashboard(request,audit_id)

def auditstop(request,audit_id):
	
	iof.stopaudit(audit_id)
	return (AuditDashboard(request,audit_id))

def download(request):
	file_path = 'data/response.csv'
	if os.path.exists(file_path):
		with open(file_path, 'rb') as fh:
			response = HttpResponse(fh.read(), content_type="text/csv")
			response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
			return response
	

	



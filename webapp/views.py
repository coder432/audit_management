from django.shortcuts import render,redirect
from django.http import HttpResponse
#...
from django.template import loader
import json
import webapp.iof as iof
#from .forms import RegisterForm

def index(request):
    return HttpResponse("Hello, world. You're at the webapp index.")

# Create your views here.

def login(request):
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


def AuditSheets(request,audit_id):
	context = {}
	context['audit_id'] = audit_id
	print(audit_id)
	sheets = iof.read_sheet(audit_id)
	context['sheet_list'] = sheets
	return render(request,'webapp/AuditSheets.html',context)


def EditAuditor(request,emp_id):
	context = {}
	print(emp_id)
	context['emp_id'] = emp_id
	return render(request,'webapp/edit_auditor.html',context)

def CreateSheet(request,audit_id):
	context = {}
	context['audit_id'] = audit_id
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

def get_sheet(request,audit_id):
	context = {}
	if request.method == 'POST':
		form  = request.POST
		context['audit_id'] = audit_id
		context['sheet_name'] = form['sheet_name']
		context['s_id'] = audit_id+form['sheet_name']
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





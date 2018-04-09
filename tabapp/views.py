from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
import json
import webapp.iof as iof
import json

# Create your views here.

def index(request):
    return HttpResponse("You're at the tapbapp index.")


def login(request):
	return render (request,'tabapp/login.html')


def SubmitResponse(request,s_id):

	context = {}
	context['s_id'] = s_id
	question_list = iof.read_questions(s_id)
	context['question_list'] = question_list



	print(question_list)

	return render(request,'tabapp/SubmitResponse.html',context)


def details(request,emp_id):

	context = {}
	d = iof.read_ongoing_audit(emp_id)
	context = d
	context['emp_id'] = emp_id
	return render(request,'tabapp/details.html',context)
	#return HttpResponse("details of audit for "+ str(context))


def show_files(request,emp_id):
	total = 0
	l = []
	status  = iof.read_status()
	context = {}
	for i in status:
		total = total + i['incomplete']
	context['total'] = total
	context['emp_id'] = emp_id
	files = iof.read_ongoing_files(emp_id)
	print(files)

	if files == 'null':
		context['message'] = 'NO FILES ALLOCATED FOR AUDITOR ' + emp_id
	

	

	remaining = {}
	for i in status:
		remaining[i['f_id']] = i['incomplete']
	for i in files:
		k = []
		k.append(i)
		k.append(remaining[i])
		l.append(k)
	files = l
	context['remaining'] = remaining 
	context['files'] = files
	print(files)
	return render(request,'tabapp/file1.html',context)

def sheets(request,emp_id,file_id):
	context = {}
	context['emp_id'] = emp_id
	context['file_id'] = file_id
	context['file_name'] = file_id[4:]
	context['a_id'] = file_id[:4]

	sheets = iof.read_sheet(file_id)
	context['sheet_list'] = sheets

	return render(request,'tabapp/sheets.html',context)

	#return HttpResponse("emp is "+emp_id+" file "+ file_id+" sheets "+str(sheets) )


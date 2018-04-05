import json
import string
import random





def password_generator(size=8, chars=string.ascii_letters + string.digits):
	 return ''.join(random.choice(chars) for i in range(size))




def read_audit(aid):
	with open("audit.txt","r") as f:
		l = json.load(f)
		print(l)
		for i in l:
			if i['audit_id'] == aid :
				return i
	
	return False 

def read_auditor(eid):

	with open("auditor.txt","r") as f:
		l = json.load(f)
		print(l)
		for i in l:
			if i['emp_id'] == eid :
				return i
	
	return False 

def del_auditor(eid):
	with open("auditor.txt","r+") as f:
		l = json.load(f)
		for i in l:
			if i['emp_id'] == eid:
				l.remove(i)
				f.seek(0)
				f.truncate()
				json.dump(l,f)
				return True

		return False

def del_audit(aid):
	with open("audit.txt","r+") as f:
		l = json.load(f)
		for i in l:
			if i['audit_id'] == aid:
				l.remove(i)
				f.seek(0)
				f.truncate()
				json.dump(l,f)
				return True

		return False

def read_sheet(f_id):
	l = []
	k = []
	with open("sheets.txt",'r') as f:
		try:
		 l = json.load(f)
		except:
		 return k

		for i in l:
		 	if i['file_id'] == f_id:
		 		k.append(i)
		return k


def read_questions(s_id):
	l = []
	k = []
	with open("questions.txt",'r') as f:
		try:
		 l = json.load(f)
		except:
		 return k

		for i in l:
		 	if i['s_id'] == s_id:
		 		k.append(i)
		return k

def read_file(aid):
	l = []
	k = []
	with open("files.txt",'r') as f:
		try:
		 l = json.load(f)
		except:
		 return k

		for i in l:
		 	if i['audit_id'] == aid:
		 		k.append(i)
		return k

def auditdetails(aid):
	with open("audit.txt","r") as f:
		l = json.load(f)
		for i in l:
			if i['audit_id'] == aid:
				return i


def read_ongoing_files(emp_id):

    
	with open("data/ongoing/Auditors.txt",'r+') as f:
		d = json.load(f)
		try:
			return d[emp_id]['files']
		except:
			return 'null'

def set_status(a_id):
	l = []
	files = read_file(a_id)
	for i in files:
		d = {}
		sheets = read_sheet(i['f_id'])
		total = len(sheets)
		complete = len([j for j in sheets if j['status']==1])
		incomplete = total - complete
		d['f_id'] = i['f_id']
		d['complete'] = complete
		d['incomplete'] = incomplete
		l.append(d)

	print(l)
	with open ('data/ongoing/status.txt','r+') as f:
		f.truncate()
		f.seek(0)
		json.dump(l,f)

def read_status():
	l = []
	with open ('data/ongoing/status.txt','r+') as f:
		l = json.load(f)
		return l






		




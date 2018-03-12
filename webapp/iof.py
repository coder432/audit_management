import json
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

def read_sheet(aid):
	l = []
	k = []
	with open("sheets.txt",'r') as f:
		try:
		 l = json.load(f)
		except:
		 return k

		for i in l:
		 	if i['file_id'] == aid:
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



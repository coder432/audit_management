import json
import string
import random
import smtplib
import csv



def password_generator(size=8, chars=string.ascii_letters + string.digits):
	 return ''.join(random.choice(chars) for i in range(size))


def send_email(email,emp_id,password):
	TO = email
	SUBJECT = 'Rajagiri Audit management'
	TEXT = 'usrername:'+emp_id+'\n password:'+password

	# Gmail Sign In
	gmail_sender = 'rsetaudit@gmail.com'
	gmail_passwd = 'Rset123!'

	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.login(gmail_sender, gmail_passwd)

	BODY = '\r\n'.join(['To: %s' % TO,
                    'From: %s' % gmail_sender,
                    'Subject: %s' % SUBJECT,
                    '', TEXT])

	try:
		server.sendmail(gmail_sender, [TO], BODY)
		print ('email sent')
	except:
		print ('error sending mail')

	server.quit()




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

#update status		
def write_sheet(l):
	with open("sheets.txt",'r+') as f:
		f.truncate()
		f.seek(0)
		json.dump(l,f)




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
def read_ongoing_audit(emp_id):
	with open("data/ongoing/Auditors.txt",'r+') as f:
		d = json.load(f)
		try:
			return auditdetails(d[emp_id]['a_id'])
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
		try:
			l = json.load(f)
		except:
			l =[]
		return l

def read_Auditor_Audit():
	with open("data/Auditor_Audit.txt","r+") as f:
		return json.load(f)

def write_Auditor_Audit(d):
	with open("data/Auditor_Audit.txt","r+") as f:
		f.truncate()
		f.seek(0)
		json.dump(d,f)

def read_Audits():
	with open("data/Audits.txt","r+") as f:
		return json.load(f)

def start_audit(aid):

	context = {}
	audit = read_audit(aid)
	set_status(aid)
	print('status is ',read_status())

	with open("data/Audits.txt","r+") as f:
		try:
			l = json.load(f)
		except:
			l = []

		l.append(aid)
		f.truncate()
		f.seek(0)
		json.dump(l,f)
		print('in audit file ',l)

	d = read_Auditor_Audit()
	auditors = d[aid]
	for i in auditors:
		det = read_auditor(i)
		#send_email(det['email'],i,det['password'])

	print('auditors assigned are ',auditors)

	ld = read_file(aid)
	files = []
	for i in ld:
		files.append(i['f_id'])
	print('files for audit id {0} are {1}'.format(aid,files))

	#chunks = [data[x:x+int(len(data)/len(m))] for x in range(0, len(data),int(len(data)/len(m)))]


	alot = [files[x:x+int(len(files)/len(auditors))] for x in range(0, len(files), int(len(files)/len(auditors)))]
	print('file splliting is ',alot)

	if len(alot) != len(auditors):
		k = alot.pop()
		alot[len(auditors)-1].extend(k)

	print('file splitting after formatting ',alot)


	with open("data/ongoing/Auditors.txt",'r+') as f:
		d = json.load(f)
	for i in auditors:
			det = {}
			det['a_id'] = aid
			det['files'] = alot.pop()
			print(det)
			d[i] = det

	print(d)
	with open("data/ongoing/Auditors.txt",'r+') as f:
		f.truncate()
		f.seek(0)
		json.dump(d,f)

def write_ongoing_sheets(d):
	with open("data/ongoing/onsheets.txt",'r+') as f:
		try:
			l = json.load(f)
		except:
			l = []

		l.extend(d)
		f.truncate()
		f.seek(0)
		json.dump(l,f)

def write_comment(d,s_id):
	with open("data/ongoing/comments.txt",'r+') as f:
		try:
			l = json.load(f)
		except:
			l ={}

		l[s_id] = d
		f.truncate()
		f.seek(0)
		json.dump(l,f)

def read_all_sheets():
	with open("sheets.txt",'r') as f:
		return json.load(f)

def stopaudit(audit_id):

	with open("sheets.txt",'r+') as f:
		l = json.load(f)
		for i in l:
			i['status'] == 0
	write_sheet(l)


	with open("data/ongoing/comments.txt",'r+') as f:
		l = {}
		f.truncate()
		f.seek(0)
		json.dump(l,f)

	with open("data/ongoing/onsheets.txt",'r+') as f:
		l = []
		f.truncate()
		f.seek(0)
		json.dump(l,f)

	with open ('data/ongoing/status.txt','r+') as f:
		l = []
		f.truncate()
		f.seek(0)
		json.dump(l,f)

	with open("data/Audits.txt","r+") as f:
		l = []
		f.truncate()
		f.seek(0)
		json.dump(l,f)

	with open("data/ongoing/Auditors.txt","r+") as f:
		l = {}
		f.truncate()
		f.seek(0)
		json.dump(l,f)

def responsecsv(audit_id):
	with open('data/response.csv', 'w+', newline='') as csvfile:
		writer = csv.writer(csvfile, delimiter=' ',quotechar=',',quoting=csv.QUOTE_ALL)
		writer.writerow([audit_id])
		d = read_Auditor_Audit()
		auditors = d[audit_id]
		for i in auditors:
			writer.writerow([i])
			files = read_ongoing_files(i)
			for j in files:
				writer.writerow([j])
				sheets = read_sheet(j)
				for k in sheets:
					writer.writerow([k['s_id'],k['sheet_name']])
					comments = json.load(open('data/ongoing/comments.txt'))
					try:
						d = comments[k['s_id']]
						row = ['comment',d['comment']]
						writer.writerow(row)
						row = ['auditee',d['auditee']]
						writer.writerow(row)
					except:
						pass

					with open("data/ongoing/onsheets.txt","r") as f:
						l = json.load(f)
						for m in l:
							if m['s_id'] == k['s_id']:
								row = [m['q'],m['q_type'],m['response']]
								print("row is "+str(row))
								writer.writerow(row)




			








    























		




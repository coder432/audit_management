import smtplib
 
def sendemail(from_addr, to_addr_list, cc_addr_list,
              subject, message,
              login, password,
              smtpserver='smtp.gmail.com:587'):
    header  = 'From: %s' % from_addr
    header += 'To: %s' % ','.join(to_addr_list)
    header += 'Cc: %s' % ','.join(cc_addr_list)
    header += 'Subject: %s'% subject
    message = header + message
 
    server = smtplib.SMTP(smtpserver)
    server.starttls()
    login = 'rset audit'

    server.login(login,password)
    problems = server.sendmail(from_addr, to_addr_list, message)
    server.quit()
if __name__ == '__main__':
    sendemail('rsetauditnoreply@gmail.com','jv241095@gmail.com','','HEello','testing','rset audit','Rset123!')
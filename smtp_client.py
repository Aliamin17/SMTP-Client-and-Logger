from socket import AF_INET, SOCK_STREAM
from socket import *
import smtplib,uuid
if __name__ == '__main__':
    print('application started')
    s=socket(AF_INET, SOCK_STREAM)
    server_address=('127.0.0.1',7779)
    s.connect(server_address)
    print('connected')
    q=input('EMAIL: ')
    w=input('PASSWORD: ')
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login(q, w)
    print('SUCCESSFULLY LOGGED IN')
    to=input('TO:')
    v=input('SUBJECT: ')
    mail=input('MAIL:')
    x = (hex(uuid.getnode()))
    host_name = gethostname()    
    IPAddress = gethostbyname(host_name)
    message = 'Subject: {}\n\n{}'.format(v, mail)
    server.sendmail(q,to,message +'\n your ip'+IPAddress+"\n MAC Address: "+x) 
    s.sendall(q.encode())
    s.sendall(v.encode())
    s.sendall(mail.encode())
    s.sendall(host_name.encode()) 
    s.sendall(IPAddress.encode()) 
    s.sendall(x.encode()) 
    
    
    s.close()
    
import smtplib
from urllib.request import urlopen
from time import sleep
def sender(cntr, ip):
    port = 25
    smtp_server = "smtp.ngs.ru"
    login = "mihail.toropov@ngs.ru"
    password = "warhammer"
    sender = "mihail.toropov@ngs.ru"
    receiver = "mihail.toropov@ngs.ru"
    message = f"""\
    Subject: Current IP adress {cntr}
    To: {receiver}
    From: {sender}
    Current IP is {ip}."""
    try:
        with smtplib.SMTP(smtp_server, port) as server:
            server.login(login, password)
            server.sendmail(sender, receiver, message)
        print('Sent')
    except:
        print('Failed send')

def reader():
    try:
        page = urlopen('http://whereismyip.org').read().strip().decode()
        return page
    except:
        return None

def whatcher(arg):
    while arg > 1:
        s = reader()
        sender(arg, s)
        new_arg = arg /2
        with open("run.cnt", 'w') as f:
            f.write(str(arg))
        sleep(arg)
        if new_arg > 1:
            arg=new_arg
        else:
            arg=2

if __name__=="__main__":
    print("Addres whatcer has started")
    try:
        with open("run.cnt", 'r') as f:
            cnt = f.read().strip()
            if cnt.isdigit():
                cnt = int(cnt)
    except FileNotFoundError:
        with open("run.cnt", 'w') as f:
            f.close()
            cnt = 654321
    whatcher(cnt)

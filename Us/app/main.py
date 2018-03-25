from __future__ import print_function
import httplib2
from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
import re,math,sys,random,os, datetime,time
import pyrebase
from collections import Counter
import hashlib
import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

fromaddr = "teamanything98@gmail.com"

config={
        "apiKey": "AIzaSyA1wjplVeOEq-19cb7QDyjlqd2TNl0iDws",
        "authDomain": "scheduleit-cc688.firebaseapp.com",
        "databaseURL": "https://scheduleit-cc688.firebaseio.com",
        "storageBucket": "scheduleit-cc688.appspot.com"
}


email = "teamanything98@gmail.com"
password = "test123"

firebase = pyrebase.initialize_app(config)
auth=firebase.auth()
user=auth.sign_in_with_email_and_password(email,password)

def refresh(user):
    user=auth.refresh(user['refreshToken'])

db=firebase.database()

def addSource(url):
    lis=db.child('Ulist').get(user['idToken']).val()
    print(lis)
    if url not in lis:
        lis.append(url)
    db.child('Ulist').set(lis,user['idToken'])

def cleanSource():
   lis=db.child('Ulist').get(user['idToken']).val()
   clist=[]
   for i in lis:
       if i!=None:
           clist.append(i)
   print(clist)
   db.child('Ulist').set(clist,user['idToken'])

def subChannel(username,value):
    try:
        data={'sub':[value]}
        users=db.child("users").order_by_key().equal_to(username).get(user['idToken'])
        if(len(users.each())):
            data=users.val()[username]
            if "sub" in data.keys():
                lis=users.val()[username]['sub']
            else:
                lis=[]
            lis.append(value)
            data['sub']=lis
            db.child("users").child(username).update(data,user['idToken'])
        else:
            db.child("users").child(username).set(data,user['idToken'])
    except:
        refresh(user)
        subChannel(username,value)

def unsubChannel(username,value):
    try:
        data={}
        users=db.child("users").order_by_key().equal_to(username).get(user['idToken'])
        if(len(users.each())):
       	    data=users.val()[username]
            if "sub" in data.keys():
                lis=data["sub"]
                if value in lis:
                    lis.remove(value)
                    data['sub']=lis
                    db.child("users").child(username).update(data,user['idToken'])
    except:
        refresh(user)
        unsubChannel(username,value)

def create_placement(name,a,b,c,d,e,f,g):
    data={}
    try:
        events=db.get(user['idToken']).val()
    except:
        refresh(user)
        events=db.get(user['idToken']).val()
    if 'Placement' in events.keys():
        lis=events['Placement']
        print(lis)
        lis[name]=[a,b,c,d,e,f,g]
        print(lis)
        try:
            db.child("Placement").set(lis,user['idToken'])
        except:
            refresh(user)
            db.child("Placement").set(lis,user['idToken'])
    else:
        data[name]=[a,b,c,d,e,f,g]
        db.child("Placement").set(data,user['idToken'])

def show_placements(username):
    try:
        placements=db.child("Placement").get(user['idToken']).val()
        users=db.child("users").child(username).get(user['idToken']).val()
    except:
        refresh(user)
        placements=db.child("Placement").get(user['idToken']).val()
        users=db.child(username).get(user['idToken']).val()
    lis={}
    print(placements)
    print(users)
    for i in placements.keys():
        print(placements[i])
        if float(users['CGPA'])>=float(placements[i][0]) and int(users['year'])>=int(placements[i][1]):
            lis[i]=placements[i]
    return lis

def Register(username,event):
    print(event)
    try:
        data={'sub':[event]}
        users=db.child("users").order_by_key().equal_to(username).get(user['idToken'])
        if(len(users.each())):#check if entry exists
            data=users.val()[username]
            if "pin" in data.keys():
                lis=data["pin"]
            else:
                lis=[]
            lis.append(event)
            data['pin']=lis
            print(data)
            db.child("users").child(username).update(data,user['idToken'])
        else:
            print(data)
            db.child("users").child(username).set(data,user['idToken'])
    except:
        refresh(user)
        Register(username,event)
    try:
        users=db.child("event").get(user['idToken']).val()
    except:
        refresh(user)
        users=db.child("event").get(user['idToken']).val()
    eventup=users[event]
    eventup[-1]=str(int(eventup[-1])+1)
    try:
        db.child("event").child(event).set(eventup,user['idToken'])
    except:
        refresh(user)
        db.child("event").child(event).set(eventup,user['idToken'])


def show_req():
    try:
        lis=db.child('requests').get(user['idToken']).val()
    except:
        refresh(user)
        lis=db.child('requests').get(user['idToken']).val()
    return lis

#inactive
def unRegister(username,event):
    try:
        data={}
        print(sender_id)
        users=db.child("users").order_by_key().equal_to(username).get(user['idToken'])
        if(len(users.each())):#check if entry exists
       	    data=users.val()[username]
            #print(data)
            if "pin" in data.keys():
                #print("here")
                lis=data["pin"]
                #print(lis)
                #print(value)
                if event in lis:
                    lis.remove(event)
                    data["pin"]=lis
                    db.child("users").child(username).update(data,user['idToken'])
    except:
        refresh(user)
        unRegister(username,event)

def generate_feed(username):
        data={}
        users=db.child("users").order_by_key().equal_to(username).get(user['idToken'])
        if(len(users.each())):
            lis=users.val()[username]
            if 'sub' in lis.keys():
                lis=lis['sub']
            else:
                return {}
            subl={}
            print(lis)
            try:
                events_per_council = db.child("council").get(user['idToken']).val()
                event=db.child("event").get(user['idToken']).val()
            except:
                refresh(user)
                generate_feed(username)
            result={}
            for i in lis:
                li=[]
                if i!=None:
                    if i in events_per_council.keys():
                        lent=len(events_per_council[i])
                        hashes=events_per_council[i][-min(lent,4):]
                        for hashe in hashes:
                        	try:
                        		li.append(event[hashe])
                        	except:
                        		print(hashe)
                result[i]=li
            return result
        else:
            return {}

def browser(council):
    try:
        articles_per_source = db.child("council").get(user['idToken']).val()
        Uarticle = db.child("event").get(user['idToken']).val()
    except:
        refresh(user)
        generate_feed(username)
    li=[]
    if council!=None:
        if council in articles_per_source.keys():
            lent=len(articles_per_source[council])
            hashes=articles_per_source[council][-min(lent,9):]
            for hashe in hashes:
                try:
                    li.append(Uarticle[hashe])
                except:
                    print(hashe)
    return li

def show_booked(username):
        data={}
        users=db.child("users").order_by_key().equal_to(username).get(user['idToken'])
        if(len(users.each())):
            lis=users.val()[username]
            if 'pin' in lis:
                lis=lis['pin']
                #print(lis)
            else:
                return []
            try:
                articles_per_source = db.child("council").get(user['idToken']).val()
                Uarticle = db.child("event").get(user['idToken']).val()
            except:
                refresh(user)
                show_booked(username)
            li=[]
            for hashe in lis:
                if hashe!=None:
                        li.append(Uarticle[hashe])
                result=li
            return result
        else:
            return []


def create_request(name,a,b,c,d,e,f,g,h,i,j):
	data={}
	try:
		events=db.get(user['idToken'])
	except:
		refresh(user)
		events=db.get(user['idToken'])
	if 'requests' in events.val().keys():
		lis=events.val()['requests']
		print(lis)
		lis[a]=[name,a,b,c,d,e,f,g,h,i,j]
		print(lis)
		try:
			db.child("requests").update(lis,user['idToken'])
		except:
			refresh(user)
			db.child("requests").update(lis,user['idToken'])
	else:
		data[a]=[name,a,b,c,d,e,f,g,h,i,j]
		db.child("requests").set(data,user['idToken'])

def create_notice(name,a,b,c,d):
    data={}
    try:
        events=db.get(user['idToken'])
    except:
        refresh(user)
        events=db.get(user['idToken'])
    if 'requests' in events.val().keys():
        lis=events.val()['requests']
        print(lis)
        lis[name]=[a,b,c,d]
        print(lis)
        try:
            db.child("requests").update(lis,user['idToken'])
        except:
            refresh(user)
            db.child("requests").update(lis,user['idToken'])
    else:
        data[name]=[a,b,c,d]
        db.child("requests").set(data,user['idToken'])

def approve_request(a):
    temp=[]
    try:
        events=db.get(user['idToken'])
    except:
        refresh(user)
        events=db.get(user['idToken'])
    if 'requests' in events.val().keys():
        lis=events.val()['requests']
        temp=lis[a]
        del lis[a]
        try:
            db.child('requests').set(lis,user['idToken'])
        except:
            refresh(user)
            db.child('requests').set(lis,user['idToken'])
    data={}
    try:
        events=db.get(user['idToken'])
    except:
        refresh(user)
        events=db.get(user['idToken'])
    temp.append('0')
    if 'event' in events.val().keys():
        lis=events.val()['event']
        lis[a]=temp
        try:
            db.child("event").update(lis,user['idToken'])
        except:
            refresh(user)
            db.child("event").update(lis,user['idToken'])
    else:
        data[a]=temp
        db.child("event").set(data,user['idToken'])
    aps=db.child("council").get(user['idToken']).val()
    tp=[a]
    if temp[0] in aps.keys():
        tp=aps[temp[0]]
        tp.append(a)
        try:
            db.child("council").child(temp[0]).set(tp,user['idToken'])
        except:
            refresh(user)
            db.child("council").child(temp[0]).set(tp,user['idToken'])
    else:
        try:
            db.child("council").child(temp[0]).set(tp,user['idToken'])
        except:
            refresh(user)
            db.child("council").child(temp[0]).set(tp,user['idToken'])
    try:
        council_email = db.child("users").get(user["idToken"]).val()
    except:
        refresh(user)
        council_email = db.child("users").get(user["idToken"]).val()
    council_email = council_email[temp[0]]["email-id"]
    title = temp[1]
    location = temp[7]
    description = temp[2]
    date_from = temp[5]
    date_to = temp[6]
    subject_text = "Approval results of your event "
    body = "Your event : " + title + " has been approved and can now be successfully hosted"
    send_text_mail(subject=subject_text,body_text=body,toaddr=council_email)
    add_remove_events("add",council_email,title,location,description,date_from,date_to)

def decline_request(a):
    temp=[]
    try:
        events=db.get(user['idToken'])
    except:
        refresh(user)
        events=db.get(user['idToken'])
    if 'requests' in events.val().keys():
        lis=events.val()['requests']
        temp=lis[a]
        del lis[a]
        try:
            db.child('requests').set(lis,user['idToken'])
        except:
            refresh(user)
            db.child('requests').set(lis,user['idToken'])

def add_user(name,cgpa,emailid,mobile):
    try:
        users=db.child("users").get(user['idToken'])
    except:
        refresh(user)
        users=db.child("users").get(user['idToken'])
    if users!=None:
        data=users.val()
        data[name]={'CGPA':cgpa,'email-id':emailid,'mobile':mobile}
        db.child("users").set(data,user['idToken'])
    else:
        data={}
        data[name]={'CGPA':cgpa,'email-id':emailid,'mobile':mobile}
        db.child("users").set(data,user['idToken'])

def remove_event(name):
    try:
        event=db.child("event").get(user['idToken']).val()
    except:
        refresh(user)
        event=db.child("event").get(user['idToken']).val()
    temp=event[name]
    del event[name]
    try:
        db.child("event").set(event,user['idToken'])
    except:
        refresh(user)
        db.child("event").set(event,user['idToken'])
    try:
        council_email = db.child("users").get(user["idToken"]).val()
    except:
        refresh(user)
        council_email = db.child("users").get(user["idToken"]).val()
    council_email = council_email[temp[0]]["email-id"]
    title = temp[1]
    location = temp[7]
    description = temp[2]
    date_from = temp[5]
    date_to = temp[6]
    subject_text = "Approval results of your event "
    body = "Unfortunately , your event : " + titile + " cannot be hosted as approved by our admin. "
    send_text_mail(subject=subject_text,body_text=body,toaddr=council_email)
    add_remove_events("del",council_email,title,location,description,date_from,date_to)

def extra(username):
    users=db.child("users").order_by_key().equal_to(username).get(user['idToken'])
    if(len(users.each())):#check if entry exists
        lis=users.val()[username]['sub']
        return lis

#### notification s
def send_sms(name,event):
    try :
        users = db.child('users').get(user['idToken']).val()
    except:
        refresh(user)
        users = db.child('users').get(user['idToken']).val()
    contact_number = users[name]["mobile"]

    import SmsBot
    query = SmsBot.sms("9820501130","password") # username is usually Mobile Number (Logging in)
    my_message = "Hi, " + name + "\nYou're successfully registered for :" + event
    query.send(contact_number,my_message) # recipient = receiver's number
    query.Logout()

def send_text_mail(subject,body_text,toaddr="nishchith.s@somaiya.edu"):
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = subject

    msg.attach(MIMEText(body_text,'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587) #465 or 587 open
    server.starttls()

    # your login details
    server.login(fromaddr, "@randombits98")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    print("Text email sent successfully")
    server.quit()

def send_mail(subject,body_text,location,toaddr = "nishchith.s@somaiya.edu"):
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = subject
    body = body_text
    msg.attach(MIMEText(body, 'plain'))

    filename = location
    attachment = open(filename, "rb")

    p = MIMEBase('application', 'octet-stream')
    p.set_payload((attachment).read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(p)

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(fromaddr, "@randombits98")
    text = msg.as_string()
    s.sendmail(fromaddr, toaddr, text)
    print("Text email sent successfully")
    s.quit()

def send_ticket(name,event):
    create_qrcode(name,event)
    try :
        users = db.child('users').get(user['idToken']).val()
    except:
        refresh(user)
        users = db.child('users').get(user['idToken']).val()
    email_id = users[name]["email-id"]
    print(email_id)
    location = name+"-"+event+"-qr.png"
    send_mail(subject="Your Confirmed Tickets for : "+event,body_text="PFA, \n regards",toaddr=email_id,location = location)

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/calendar-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/calendar'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Calendar API Python Quickstart'


def get_credentials():
    try:
        import argparse
        flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
    except ImportError:
        flags = None
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'calendar-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def add_remove_events(flag,council_email,title,location,description,df,dt):
    """Shows basic usage of the Google Calendar API.

    Creates a Google Calendar API service object and outputs a list of the next
    10 events on the user's calendar.
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)

    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    eventsResult = service.events().list(
        calendarId='primary', timeMin=now, maxResults=10, singleEvents=True,
        orderBy='startTime').execute()

    events = eventsResult.get('items', [])
    if flag == "del":
        for event in events:
            if event["summary"] == title:
                service.events().delete(calendarId='primary', eventId=event["id"]).execute()
                return

    created_event = service.events().quickAdd(
    calendarId='primary',
    text='Appointment at Somewhere on June 3rd 10am-10:25am').execute()
    print('Creating events')

    '''
    check :meta , add params
    '''
    #mm/dd/yyyy/hh:mm:am
    date_from = df + "00:-05:30" # df[6:10] + "-" + df[:2] + "-" + df[3:5] + "T" + df[11:13] + ":" + df[14:16] + ":00-05:30"
    date_to = dt + "00:-05:30" # dt[6:10] + "-" + dt[:2] + "-" + dt[3:5] + "T" + dt[11:13] + ":" + dt[14:16] + ":00-05:30"
    event = {
        'summary': title,
        'location': location,
        'description': description,
        'start': {
        'dateTime': date_from,
        'timeZone': 'America/Los_Angeles',
        },
        'end': {
        'dateTime': date_to,
        'timeZone': 'America/Los_Angeles',
        },
        'recurrence': [
        'RRULE:FREQ=DAILY;COUNT=1'
        ],
        'attendees': [
            {'email': council_email},
        ],
        'reminders': {
        'useDefault': False,
        'overrides': [
        {'method': 'email', 'minutes': 24 * 60},
        {'method': 'popup', 'minutes': 10},
        ],
    },
    }

    if flag == "add":
        event = service.events().insert(calendarId='primary', body=event).execute()

    '''
    if not events:
        print('No upcoming events found.')
    for event in events:
        print(event)
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])
    '''

def create_qrcode(name,eventname):
    import pyqrcode
    qr = pyqrcode.create("Name: "+name+" \nApproved: Yes \n" + "Event Name: "+eventname)     # expand
    qr.png(name+"-"+eventname+"-qr.png", scale=5)

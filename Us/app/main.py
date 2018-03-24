import re,math,sys
import pyrebase
from collections import Counter
import os, datetime
import random
import hashlib
import time
import pandas as pd

config={
        "apiKey": "AIzaSyA1wjplVeOEq-19cb7QDyjlqd2TNl0iDws",
        "authDomain": "scheduleit-cc688.firebaseapp.com",
        "databaseURL": "https://scheduleit-cc688.firebaseio.com",
        "storageBucket": "scheduleit-cc688.appspot.com"
}


email=""
password=""

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

def Register(username,event):
    print(event)
    try:
        users=db.child("id").order_by_key().equal_to(username).get(user['idToken'])
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
def create_request(name,a,b,c,d):
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
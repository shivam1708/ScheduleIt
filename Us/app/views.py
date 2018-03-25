from django.shortcuts import render,redirect
from app.forms import UserForm,UserProfileInfoForm,CouncilForm
from app.models import UserProfileInfo
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from . import main

from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'app/index.html')

def student(request):
    return render(request,'app/student.html')

def student_remove(request):
    if request.method == 'POST':
        searched = request.POST.get('sub')
        main.unsubChannel(str(request.user),searched)
    return HttpResponseRedirect(reverse('app:subscribed'))


def student_add(request):

    if request.method == 'POST':
        searched = request.POST.get('add')
        main.subChannel(str(request.user),searched)
    return HttpResponseRedirect(reverse('app:subscribed'))

def subscribed(request):
    listo = main.extra(str(request.user))
    print(listo)
    return render(request,'app/list.html',{'listo':listo})

def student_showsub(request):
    src=[]
    #print(users[i],id)
    li=main.show_booked(str(request.user))
    #print(li)
    for i in li:
        print(i)
        try:
            print("Bello")
            src.append([i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10]])
        except:
            pass
        #desc.append(summ)
    print(len(src))
    return render(request,'app/show.html',{'src':src})
    #return render(request,'basic_app/user_page.html',{'src':src})
    #return render(request,'app/show.html',{'src':src})

def student_enter(request):
    return render(request,'app/index2.html',{})

def student_browse(request):
    if request.method == 'POST':
        source=request.POST.get('inputurl2')
    src = []
    li=main.browser(source)
    print("+++++++++++++++++++",source,"++++++++++++++++++")
    print(li)
    for el in li:
        try:
            src.append([el[0],el[1],el[2],el[3],el[4],el[5],el[6],el[7],el[8],el[9],el[10]])
        except:
            pass
    print(len(src))
    return render(request,'app/browse.html',{'src':src})

def register(request):
    print("hello")
    if request.method == 'POST':
        searched = request.POST.get('add')
        main.Register(str(request.user),searched)
        main.send_ticket(request.user,searched)

        #return redirect(u)
        #print(searched)
    return HttpResponse("done")
    #return HttpResponseRedirect(reverse('app:mylist'))

def addEvent(request):
    print("hello")
    if request.method == 'POST':
        searched = request.POST.get('add')
        main.approve_request(searched)
        #print(searched)
    return HttpResponse("done")
    #return HttpResponseRedirect(reverse('app:mylist'))

def unregister(request):
    print("hello3")
    if request.method == 'POST':
        searched = request.POST.get('add')
        print(searched,"shivamxxxxxxxxxxxxxxxxxxxxxxx")
        main.unRegister(str(request.user),searched)
        print(searched)
        #print(searched)
    return HttpResponseRedirect(reverse('app:student_showsub'))

def removeEvent(request):
    print("hello3")
    if request.method == 'POST':
        searched = request.POST.get('add')
        print(searched,"shivamxxxxxxxxxxxxxxxxxxxxxxx")
        main.decline_request(searched)
        print(searched)
        #print(searched)
    # return HttpResponseRedirect(reverse('app:admin_fire'))
    return HttpResponse("removed")


@login_required
def student_fire(request,id):
    users = User.objects.all()

    # cname = []
    # title = []
    # head = []
    # desc = []
    # pre = []
    # cost = []
    # img = []

    for i in range(len(users)):
        src=[]
        print(users[i],id)
        if(str(users[i]) == id):
            li=main.generate_feed(id)
            print(li)
            for i in li.keys():
                #print(i)
                for el in li[i]:
                    try:
                        src.append([i,el[1],el[2],el[3],el[4],el[5],el[6],el[7],el[8],el[9],el[10]])
                    except:
                        pass
                    #desc.append(summ)
            print(len(src))

            return render(request,'app/studentuser.html',{'src':src})
        #return render(request,'basic_app/user_page.html',{'src':src})
    return render(request,'app/studentuser.html',{'src':src})

@login_required
def student_user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('index'))

def student_register(request):

    registered = False

    if request.method == 'POST':


        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()

            user.set_password(user.password)

            user.save()

            profile = profile_form.save(commit=False)

            profile.user = user

            if 'profile_pic' in request.FILES:
                print('found it')
                # If yes, then grab it from the POST form reply
                profile.profile_pic = request.FILES['profile_pic']

            # Now save model
            profile.save()
            print(user.username,user.email,profile.phone_no)
            main.add_user(user.first_name,profile.pointer,user.email,profile.phone_no)
            # Registration Successful
            registered = True
            u = reverse('app:student_user_login')
            return HttpResponseRedirect(u)
            hashcode = 0
            name = user.username
            size = len(name)
            temp = size
            for i in name:
                hashcode += ord(i)*(10**temp)
                temp-=1
            #print(hashcode)
            #subscribe.addUser(str(hashcode),name)

        else:
            # One of the forms was invalid if this else gets called.
            print(user_form.errors)

    else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request,'app/studentregistration.html',
                          {'user_form':user_form,
                            'profile_form':profile_form,
                           'registered':registered})

def student_user_login(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        print(request.user.username)


        user = authenticate(username=username, password=password)


        if user:

            if user.is_active:

                login(request,user)
                print(user)
                u = reverse('app:student_fire',kwargs={'id':user})
                return HttpResponseRedirect(u)
            else:
                return HttpResponse("Your account is not active.")
        else:
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, 'app/studentlogin.html', {})

def registerevent(request):
    registered = False
    if request.method == 'POST':
        name = request.POST.get('name')
        short = request.POST.get('short')
        long = request.POST.get('long')
        pre = request.POST.get('pre')
        indate = request.POST.get('indate')
        outdate = request.POST.get('outdate')
        location = request.POST.get('location')
        image = request.POST.get('image')
        cost = request.POST.get('cost')
        payment = request.POST.get('payment')
        print(str(indate),str(outdate))
        #do processing over
        main.create_request(str(request.user),str(name),str(short),str(long),str(pre),str(indate),str(outdate),str(location),str(image),str(cost),str(payment))
        registered = True
    return render(request,'app/registerevent.html',{'registered':registered})

def placement(request):
    registered = False
    if request.method == 'POST':
        name = request.POST.get('name')
        pointer = request.POST.get('pointer')
        year = request.POST.get('year')
        no = request.POST.get('no')
        pos = request.POST.get('pos')
        desc = request.POST.get('desc')
        date = request.POST.get('date')
        url = request.POST.get('url')
        #do processing over
        main.create_placement(str(name),str(pointer),str(year),str(no),str(pos),str(desc),str(date),str(url))
        registered = True
    return render(request,'app/placement.html',{'registered':registered})

def placementlist(request):
    li = main.show_placements(request.user)
    src = []
    for i in li.keys():
        src.append([i,li[i][2],li[i][3],li[i][4],li[i][5],li[i][6]])
    return render(request,'app/placementlist.html',{'src':src})

@login_required
def council_fire(request,id):
    src=[]
    li=main.browser(id)
    print(li)
    for el in li:
        try:
            #print(el[11])  count
            src.append([id,el[1],el[2],el[3],el[4],el[5],el[6],el[7],el[8],el[9],el[10],el[11]])
        except:
            pass
    print(len(src))
    return render(request,'app/counciluser.html',{'src':src})
    # if str(id)==str(request.user):
    #     return render(request,'app/counciluser.html',{'name':str(id)})
    # else:
    #     return HttpResponse("Cannot access")


@login_required
def council_user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('index'))

def council_register(request):

    registered = False

    if request.method == 'POST':


        user_form = CouncilForm(data=request.POST)

        if user_form.is_valid():

            user = user_form.save()

            user.set_password(user.password)

            user.save()

            # Registration Successful
            registered = True
            u = reverse('app:council_user_login')
            return HttpResponseRedirect(u)
            hashcode = 0
            name = user.username
            size = len(name)
            temp = size
            for i in name:
                hashcode += ord(i)*(10**temp)
                temp-=1
            #print(hashcode)
            #subscribe.addUser(str(hashcode),name)

        else:
            # One of the forms was invalid if this else gets called.
            print(user_form.errors)

    else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form = CouncilForm()

    return render(request,'app/councilregistration.html',
                          {'user_form':user_form,
                           'registered':registered})

def council_user_login(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')



        user = authenticate(username=username, password=password)


        if user:

            if user.is_active:

                login(request,user)
                print(user)
                u = reverse('app:council_fire',kwargs={'id':user})
                return HttpResponseRedirect(u)
            else:
                return HttpResponse("Your account is not active.")
        else:
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, 'app/councillogin.html', {})

@login_required
def admin_user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('index'))

@login_required
def admin_fire(request,id):
    print("Hello")
    li = main.show_req()
    #print(li)
    src=[]
    for i in li.keys():
        #print(i)
        try:
            #print([i,li[i][1],li[i][2],li[i][3],li[i][4],li[i][5],li[i][6],li[i][7],li[i][8],li[i][9],li[i][10]])
            src.append([li[i][0],li[i][1],li[i][2],li[i][3],li[i][4],li[i][5],li[i][6],li[i][7],li[i][8],li[i][9],li[i][10]])
        except:
            pass
            #desc.append(summ)
    print(len(src))

    #return render(request,'app/studentuser.html',{'src':src})
    return render(request,'app/adminuser.html',{'src':src})

def admin_user_login(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        if(username != 'main'):
            return HttpResponse("Cannot access")

        user = authenticate(username=username, password=password)


        if user:

            if user.is_active:
                login(request,user)
                print(user)
                u = reverse('app:admin_fire',kwargs={'id':user})
                return HttpResponseRedirect(u)
            else:
                return HttpResponse("Your account is not active.")
        else:
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, 'app/adminlogin.html', {})

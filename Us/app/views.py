from django.shortcuts import render
from app.forms import UserForm,UserProfileInfoForm,CouncilForm
from app.models import UserProfileInfo
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse


from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'app/index.html')

def student(request):
    return render(request,'app/student.html')

@login_required
def student_fire(request,id):
    if str(id)==str(request.user):
        return render(request,'app/studentuser.html',{'name':str(id)})
    else:
        return HttpResponse("Cannot access")

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

@login_required
def council_fire(request,id):
    if str(id)==str(request.user):
        return render(request,'app/counciluser.html',{'name':str(id)})
    else:
        return HttpResponse("Cannot access")

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
    if str(id)==str(request.user):
        return render(request,'app/adminuser.html',{'name':str(id)})
    else:
        return HttpResponse("Cannot access")

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

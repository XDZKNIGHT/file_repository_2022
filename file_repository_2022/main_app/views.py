import email
from multiprocessing import context
from typing import Dict
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from main_app.models import Profiles
# Create your views here.


def index(request):
    # Login
    if request.method == 'POST':
        
        #Clear Log out session
        if('Logged-out' in request.POST):
            del request.session['logged_username']
            del request.session['logged_email']
            del request.session['logged_id']
            del request.session['logged_user_type']

        try:
            if "@" in request.POST['user-email']:
                found = Profiles.objects.get(eMail=request.POST['user-email'], password=request.POST['pwd'])
            else:
                found = Profiles.objects.get(username=request.POST['user-email'], password=request.POST['pwd'])
            request.session['logged_username'] = found.username
            request.session['logged_email'] = found.eMail
            request.session['logged_id'] = found.id
            if(found.admin and request.POST['user-type']=="Admin"):
                request.session['logged_user_type'] = found.admin
                return render(request, 'AdminHomepage.html')
            elif(not found.admin and request.POST['user-type']=="User"):
                request.session['logged_user_type'] = found.admin
                return render(request, 'UserHomepage.html')
        except:
            return render(request, 'index.html')
#Redirect to page if user did not log out properly
    if('logged_user_type' in request.session):
        if(request.session['logged_user_type'] == True):
            return render(request, 'AdminHomepage.html')
        else:
            return render(request, 'UserHomepage.html')
    
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        found = Profiles.objects.filter(eMail=request.POST['email'], username= request.POST['userName'])
        if(not found):
            p = Profiles(username = request.POST['userName'], 
            eMail = request.POST['email'], 
            password = request.POST['password'], 
            security_question = request.POST['SQuestion'], 
            security_answer = request.POST['SAnswer'], )
            p.save()
            return render(request, 'index.html')
        else:
            # insert alert if register failed
            pass
    return render(request, 'register.html')

def AdminHomepage(request):
    #Check if Logged in
    # if('logged_email' not in request.session):
    #     return render(request, 'index.html')
    # found = Profiles.objects.get(id=request.session['logged_id'])
    context = CheckLoggedIn(request)
    return render(request, 'AdminHomepage.html',context)

def UserHomepage(request):
    context = CheckLoggedIn(request)
    return render(request, 'UserHomepage.html',context)

def UserProfile(request):
    try:
        profile = Profiles.objects.get(id = request.session['logged_id'])
    except:
        pass
    context = {'username':profile.username, 'email': profile.eMail, 'picture':profile.profile_picture}
    return render(request, 'UserProfile.html',context)

def UserChangePassword(request):
    if('logged_email' not in request.session):
        return render(request, 'index.html')
    found = Profiles.objects.get(id=request.session['logged_id'])

    if request.method == 'POST':
        if request.POST['CurrentPass'] == found.password and request.POST['NewPass'] == request.POST['CNewPass']:
            found.password = request.POST['NewPass']
            found.save()
        else:
            #insert alert
            pass
    context = {'picture':found.profile_picture}
    return render(request, 'UserChangePassword.html',context)

def UserEditAccount(request):
    try:
        profile = Profiles.objects.get(id = request.session['logged_id'])

        context = {'username':profile.username, 'email':profile.eMail, 'picture':profile.profile_picture}
    except:
        pass
    if request.method == 'POST':
        try:
            userEditFound = Profiles.objects.filter(eMail = request.POST['NewUserEmail'], username=request.POST['NewUserUsername'])
            
            #Data validation for existing accounts
            if profile.password==request.POST['UserPassword']:
                profile.username = request.POST['NewUserUsername']
                profile.eMail = request.POST['NewUserEmail']
                profile.save()
                context['username'] = profile.username
                context['email'] = profile.eMail
                if(not request.FILES['UserPFP']==''):
                    profile.profile_picture = request.FILES['UserPFP']
                    profile.save()
                context['picture'] = profile.profile_picture
                
        except:
            pass
        
    return render(request, 'UserEditAccount.html',context)

def UserArchive(request):
    context = CheckLoggedIn(request)
    return render(request, 'UserArchive.html',context)

def AdminProfile(request):
    return render(request, 'AdminProfile.html')

def AdminEditAccount(request):
    return render(request, 'AdminEditAccount.html')

def AdminChangePassword(request):
    return render(request, 'AdminChangePassword.html')

def AdminArchive(request):
    context = CheckLoggedIn(request)
    return render(request, 'AdminArchive.html', context)

def AdminUserTab(request):
    context = CheckLoggedIn(request)
    return render(request, 'AdminUserTab.html', context)

def AdminFileArchive(request):
    context = CheckLoggedIn(request)
    return render(request, 'AdminFileArchive.html', context)

def AdminCreateUser(request):
    return render(request, 'AdminCreateUser.html')

def AdminEditUser(request):
    return render(request, 'AdminEditUser.html')



def CheckLoggedIn(request) -> Dict:
    if('logged_email' not in request.session):
        return render(request, 'index.html')
    user = Profiles.objects.get(id=request.session['logged_id'])

    allContext = {'username' : user.username,'email' : user.eMail,'profile_picture': user.profile_picture}
    return allContext
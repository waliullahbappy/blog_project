from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import  login,authenticate,logout
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm
from app_login.forms import UserProfileChange,ProfilePic


# Create your views here.

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request,'Username Already Exists!')
            elif User.objects.filter(email=email).exists():
                messages.error(request,'email Already Exists!')

            else:
                user=User.objects.create_user(username=username,password=password,email=email)
                user.save()
                messages.success(request, 'Your Registration successfully Done!',)
                
                     
        else:
            messages.error(request,'password & confirm password is not match !') 
    diction={}
    return render(request,'signup.html', context=diction)

def user_login(request):
    form = AuthenticationForm()
    if request.method =='POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse('home'))

    diction = {'form':form}
    return render(request, 'login.html',context=diction)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


@login_required
def profile(request):
    diction={}
    return render(request,'profile.html', context=diction)

@login_required
def user_profile_change(request):
    current_user = request.user
    form = UserProfileChange(instance=current_user)
    if request.method == 'POST':
        form = UserProfileChange(request.POST,instance=current_user)
        if form.is_valid():
            form.save()
            form = UserProfileChange(instance=current_user)
    diction={'form':form}
    return render(request,'change_profile.html',context=diction)


@login_required
def password_change(request):
    current_user = request.user
    changed = False
    form = PasswordChangeForm(current_user)
    if request.method =='POST':
        form = PasswordChangeForm(current_user, data=request.POST)
        if form.is_valid():
            form.save()
            changed = True

    diction={'form':form,'changed':changed}
    return render(request,'change_pass.html',context=diction)

@login_required
def add_profile_pic(request):
    form = ProfilePic()
    if request.method=='POST':
        form=ProfilePic(request.POST,request.FILES)
        if form.is_valid():
            user_obj=form.save(commit=False)
            user_obj.user = request.user
            user_obj.save()
            return HttpResponseRedirect(reverse('app_login:profile'))
    return render(request,'add_profile_pic.html',context={'form':form})

@login_required
def change_profile_pic(request):
    form=ProfilePic(instance=request.user.user_profile)
    
    if request.method=='POST':
        form=ProfilePic(request.POST,request.FILES,instance=request.user.user_profile)
        if form.is_valid():
            form.save()
            messages.info(request, 'Successfully Image Updates ...........!',)
            return HttpResponseRedirect(reverse('app_login:profile'))
    diction={
                'form':form,
                
                }
    return render(request,'add_profile_pic.html',context=diction)
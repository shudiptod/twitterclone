from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.models import User
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created for {username}.')
            return redirect('login')
    else:
        form = UserRegisterForm(initial={'username':"shudipto",'email':"shudpto111@gmail.com",'password1':"password0099",'password2':"password0099"})

    return render (request,'user/register.html', {'form':form})

@login_required
def profile(request):
    if request.method == 'POST':
        uform = UserUpdateForm(request.POST,instance=request.user)
        pform = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if uform.is_valid and pform.is_valid:
            uform.save()
            pform.save()
            messages.success(request, f'Account Has Been Updated.')
            return redirect ('profile')
    else:
        uform = UserUpdateForm(instance=request.user)
        pform = ProfileUpdateForm(instance=request.user)

    return render(request,'user/profile.html', {'uform':uform,'pform':pform})

@login_required
def search(request):
    if request.method == 'POST':
        khujbo = request.POST.get('search')
        results = User.objects.filter(username__contains=khujbo)
        return render(request,'user/search_result.html',{'results':results})
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
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
        form = UserRegisterForm()

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
        pform = ProfileUpdateForm(instance=request.user.profile)

    return render(request,'user/profile.html', {'uform':uform,'pform':pform})


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import ExtendedUserCreationForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = ExtendedUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            user = authenticate(username=username,password=password)
            login(request, user)

            return redirect('index')

    else:
        form = ExtendedUserCreationForm()
    return render(request, 'profileapp/register.html', {'form':form})

@login_required
def profile(request):
    return render(request, 'profileapp/profile.html')
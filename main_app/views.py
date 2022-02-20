from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login





def signup(request):

    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            error_message = 'invalid credentials - please try again'

    form = UserCreationForm
    context = {'form': form, 'error': error_message}
    return render(request, 'registration/signup.html', context)

def home(request):
    return render(request, 'home.html')



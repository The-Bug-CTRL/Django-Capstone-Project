# candidate/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .forms import LoginForm
from .models import Poll
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            print("User created and logged in:", user.username)
            return redirect('user_login')  # Redirect to the login page after registration
        else:
            print("Form is not valid:", form.errors)
    else:
        form = UserCreationForm()

    return render(request, 'candidate/registration/register.html', {'form': form})



def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to the home page after successful login
            else:
                form.add_error(None, 'Invalid username or password.')
    else:
        form = LoginForm()

    return render(request, 'candidate/login.html', {'form': form})

@login_required
def home(request):
    polls = Poll.objects.all()
    return render(request, 'candidate/home.html', {'polls': polls})

def page(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, f'candidate/page{poll_id}.html', {'poll': poll})

def vote(request, poll_id):
    if request.method == 'POST':
        poll = get_object_or_404(Poll, pk=poll_id)
        selected_choice = request.POST.get('choice', None)
        valid_choices = ['option1', 'option2']

        if selected_choice in valid_choices:
            # Process the vote here (you may want to update the Poll model)
            return redirect(reverse('home'))
        else:
            return HttpResponse('Invalid choice')
    else:
        return HttpResponse('Invalid request')

def poll(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'candidate/polls/poll.html', {'poll': poll})
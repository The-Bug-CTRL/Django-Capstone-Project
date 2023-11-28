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
    """
    View for user registration.

    If the request method is POST, it processes the registration form.
    If the form is valid, a new user is created, logged in, and redirected to the login page.
    If the form is not valid, error messages are printed.

    If the request method is GET, it renders the registration form.

    :param request: HTTP request object.
    :return: Rendered HTML template with the registration form.
    """
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
    """
    View for user login.

    If the request method is POST, it processes the login form.
    If the form is valid, the user is authenticated and logged in, then redirected to the home page.
    If the form is not valid, an error message is added to the form.

    If the request method is GET, it renders the login form.

    :param request: HTTP request object.
    :return: Rendered HTML template with the login form.
    """
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
    """
    View for the home page.

    Requires the user to be logged in.
    Retrieves all polls and renders the home page.

    :param request: HTTP request object.
    :return: Rendered HTML template with the home page.
    """
    polls = Poll.objects.all()
    return render(request, 'candidate/home.html', {'polls': polls})


def page(request, poll_id):
    """
    View for displaying a specific poll page.

    Retrieves the poll with the given poll_id and renders the corresponding page template.

    :param request: HTTP request object.
    :param poll_id: ID of the poll to display.
    :return: Rendered HTML template for the specific poll page.
    """
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, f'candidate/page{poll_id}.html', {'poll': poll})


def vote(request, poll_id):
    """
    View for processing user votes.

    If the request method is POST, it processes the vote.
    Validates the selected choice and redirects to the home page.

    :param request: HTTP request object.
    :param poll_id: ID of the poll for which the vote is being processed.
    :return: Redirect to the home page or an error response.
    """
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
    """
    View for displaying a specific poll.

    Retrieves the poll with the given poll_id and renders the poll template.

    :param request: HTTP request object.
    :param poll_id: ID of the poll to display.
    :return: Rendered HTML template for the specific poll.
    """
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'candidate/polls/poll.html', {'poll': poll})

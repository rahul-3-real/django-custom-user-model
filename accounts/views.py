from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import PasswordChangeView, PasswordResetDoneView
from django.contrib.auth.decorators import login_required
from datetime import datetime

# Create your views here.


@login_required
def index(request):
    date_today = datetime.now().date()
    template_name = 'index.html'
    context = {
        'date': date_today
    }
    return render(request, template_name, context)


def login_view(request):
    form = AuthenticationForm()
    err_msg = None
    template_name = 'accounts/login.html'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None and user.is_director == False:
            login(request, user)
            if request.GET.get('next'):
                return redirect(request.GET.get('next'))
            else:
                return redirect('index')
        else:
            err_msg = 'Oops!, Something went wrong, are you sure you are a producer'
    context = {
        'form': form,
        'err_msg': err_msg
    }
    return render(request, template_name, context)


def logout_view(request):
    logout(request)
    return redirect('login')


class PasswordChange(PasswordChangeView):
    template_name = 'accounts/change-password.html'
    success_url = reverse_lazy('password-updated')


class PasswordResetDone(PasswordResetDoneView):
    template_name = 'accounts/password-success.html'

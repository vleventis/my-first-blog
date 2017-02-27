from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.template import loader
from .models import *
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib.auth.models import AbstractUser



@login_required()
def index(request):
    user = request.user
    return render(request, 'index.html', {'user': user})


@login_required()
def get_credit(request):
    user = request.user
    if request.method == 'POST':
        form = CreditForm(request.POST)
        if form.is_valid():
            user.credits += form.cleaned_data['your_credit']
            user.save()
            return HttpResponseRedirect('/thanks/')

    else:
        form = CreditForm()
    return render(request, 'credit.html', {'form': form})

@login_required()
def call_history(request):

    user = request.user
    calls = Call.objects.all().filter(user=user)

    return render(request, 'call_history.html', {'calls': calls})

@login_required()
def usage(request):
    user = request.user
    if request.method == 'POST':
        form = TeleForm(request.POST)
        if form.is_valid():
            newcall = Call.objects.create(user=user,
                                          duration=form.cleaned_data['your_duration'],
                                          target_no=form.cleaned_data['your_call'],
                                          timeofcall=timezone.now())
            newcall.save()
            user.credits -= form.cleaned_data['your_duration'] * newcall.rate
            user.save()
            return HttpResponseRedirect('/thanks/')
    else:
        form = TeleForm()
    return render(request, 'usage.html', {'form': form})
















# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Team
from forms import RegistrationForm

import datetime

def home(request):
    return render_to_response('home.html')

def brackets(request):
    return render_to_response('brackets.html')

def schedule(request):
    return render_to_response('schedule.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            c = form.cleaned_data
            teamname = c['teamname']
            instance = form.save(commit=False)
            instance.save()
            if c['division'] == u'P':
                div = '<option value="Premier">Premier $450.00 USD</option>'
            elif c['division'] == u'M':
                div = '<option value="Club">Club $375.00 USD</option>'
            elif c['division'] == u'O':
                div = '<option value="Old Boys">Old Boys $350.00 USD</option>'
            elif c['division'] == u'W':
                div = '<option value="Women">Women $300.00 USD</option>'
            else:
                pass; # should not occur since division has been validated
            name = '<input type="hidden" name="on1" value="Club Name"></td></tr><tr><td><input type="hidden" name="os1" maxlength="200" value="' + c['teamname'] + '">'

            return render_to_response('paypal.html', {'teamname':str(teamname), 'div':div, 'name':name})
        else:
            return render_to_response('register.html', {'form':form}, context_instance=RequestContext(request))
    else:
        form = RegistrationForm()
    return render_to_response('register.html', {'form':form}, context_instance=RequestContext(request))

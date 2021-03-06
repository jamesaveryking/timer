from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
import datetime, json
from . import forms
from .models import TimerRequest, User
# Create your views here.
def timeReport(request):
    req = request
    context = {}
    if(request.method == "GET"):
        initialValues = {
            "timerLabel" : "Edit Label Here",
            "start_switch" : False,
            "end_switch" : False,
            "start_primer" : False,
            "end_primer" : False
        }
        context["success"] = str(request.method)
        context["form"] = forms.TimerForm(initialValues)
        template = loader.get_template("timer.html")
        return HttpResponse(template.render(context, request))
    elif(request.method == "POST"):
        form = forms.PrayerForm(request.POST)
        if form.is_valid():
            initialValues = {
                "p_topic" : "General",
                "p_request" : "Please Describe Your Request",
                "p_intention" : "Please Describe Your Intention",
                "p_timestamp" : datetime.date.today(),
                "p_status" : False
            }
            category = form.cleaned_data.get('p_category')
            #validate category
            description = form.cleaned_data.get('p_description')
            #validate description
            intention = form.cleaned_data.get('p_intention')
            #validate intention, could be the same validation as description
            initiated = form.cleaned_data.get('p_initiated')
            #validate initiated time
            answered = form.cleaned_data.get('p_answered')
            #validate answered
            verses = form.cleaned_data.get('p_verses')
            #validate intention, could be the same validation as description
            userid = form.cleaned_data.get('p_userid')
            #validate userid -- temporary representation of what will be in the token
            userfirstname = form.cleaned_data.get('p_userfirstname')
            #validate firstName -- temporary representation of what will be in the token
            userInstance = User.objects.filter(first_name=userfirstname).get()
            #validate userInstance -- temporary representation of what will be in the token
            r = PrayerRequest(user=userInstance,r_intention=intention,r_description=description,r_category=category,r_initiated=initiated,r_verses=verses,r_answered=answered)
            r.save()
            context["success"] = "Successfully Updated Prayer Log"
            context["category"] = category
            template = loader.get_template("success.html")
            return HttpResponse(template.render(context, request))
        else:
            context["error"] = 'Invalid Form'
            template = loader.get_template("error.html")
            return HttpResponse(template.render(context, request))
    else:
        context["error"] = str(request.method)
        template = loader.get_template("error.html")
        return HttpResponse(template.render(context, request))

def individualLog(request):
    context = {}
    if(request.method == "GET"):
        pastRequests = PrayerRequest.objects.order_by('-r_initiated')[:5]
        context["success"] = str(request.method)
        context["pastRequests"] = pastRequests
        template = loader.get_template("individualLog.html")
        return HttpResponse(template.render(context, request))
    else:
        context["error"] = str(request.method)
        template = loader.get_template("error.html")
        return HttpResponse(template.render(context, request))

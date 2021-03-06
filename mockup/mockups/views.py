from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
import datetime, json
from . import forms
# Create your views here.
def mockup(request):
    context = {}
    if(request.method == "GET"):
        initialValues = {
            "timerLabel" : "Edit Label Here",
            "start_primer" : False,
            "end_primer" : False
        }
        context["success"] = str(request.method)
        context["form"] = forms.TimerForm(initialValues)
        template = loader.get_template("timer.html")
        return HttpResponse(template.render(context, request))
    else:
        context["error"] = str(request.method)
        template = loader.get_template("error.html")
        return HttpResponse(template.render(context, request))

def mockupLog(request):
    context = {}
    if(request.method == "GET"):
        context["success"] = str(request.method)
        template = loader.get_template("mockupLog.html")
        return HttpResponse(template.render(context, request))
    else:
        context["error"] = str(request.method)
        template = loader.get_template("error.html")
        return HttpResponse(template.render(context, request))

def mockupUser(request):
    context = {}
    if(request.method == "GET"):
        context["success"] = str(request.method)
        context["form"] = forms.UserForm()
        template = loader.get_template("mockupUser.html")
        return HttpResponse(template.render(context, request))
    else:
        context["error"] = str(request.method)
        template = loader.get_template("error.html")
        return HttpResponse(template.render(context, request))

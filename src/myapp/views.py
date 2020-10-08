from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from myapp.forms import TaskForm,UserAddForm
from myapp.models import Task
from django.forms.models import model_to_dict
from time import time
import json
from django.core import serializers
from myapp.models import MyUser

# In this section Ajax is been used to display data in a realtime manner
def IndexView(request):
	context={

	}
	return render(request,'myapp/index.html',context)
def AjaxIndexView(request):
	qs=MyUser.objects.all()[:20]
	return JsonResponse({'users':list(qs.values())})
# In this section Ajax is been used to submit data that is displayed in the above section
def UserAddView(request):
	form=UserAddForm()
	context={
	'form':form
	}
	return render(request,'myapp/useradd.html',context)
def AjaxUserAddView(request):
	if request.method=="POST" and request.is_ajax():
		form=UserAddForm(request.POST or None, request.FILES or None)
		form.save()
		return JsonResponse({'success':True},status=200)
	return JsonResponse({'success':False},status=400)
# Ajax Form Submission and Realtime data display
def TaskList(request):
	form=TaskForm()
	tasks=Task.objects.all().order_by('-date')
	context={
	'form':form,
	'tasks':tasks
	}
	return render(request,'myapp/list.html',context)
def AjaxTaskList(request):
    if request.method=="POST" and request.is_ajax():
        form=TaskForm(request.POST,request.FILES or None)
        new_task=form.save()
        return JsonResponse({'task':model_to_dict(new_task)},status=200)
    return JsonResponse({"success":False},status=400)
# =====================================IDK=
def TaskDisplay(request):
	task=Task.objects.all()
	context={
	'task':task
	}
	return render(request,'myapp/display.html',context)
def AjaxTaskDisplay(request):
	# text=request.Get('button_text')
	if request.method=="GET" and request.is_ajax():
		# t=serializers.serialize('json', Task.objects.all())
		t=time()
		return JsonResponse({'seconds':t},status=200)
	return JsonResponse({'success':False},status=400)

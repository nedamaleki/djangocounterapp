from django.shortcuts import render,redirect
from .models import TodoModel
from .forms import TodoModelForm
from django.contrib import messages
from django.http import HttpResponseRedirect

def todoview (request):
	
	all_tasks = TodoModel.objects.all
	context = {'alltasks': all_tasks}
	return render(request, 'homepage.html', context)

def addtask (request):
	import requests
	import json

	if request.method == 'POST':
		task=TodoModelForm(request.POST or None)
		if task.is_valid():
			task.save()
			messages.success(request, ("Task Has Been Added"))

	return redirect ('todoview')

def deletetask(request,task_id):
	item = TodoModel.objects.get(pk=task_id)
	item.delete()
	messages.success(request,'Task Has Been Deleted!')
	return redirect('todoview')

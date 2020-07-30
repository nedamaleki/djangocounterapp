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
	task = TodoModel.objects.get(pk=task_id)
	task.delete()
	messages.success(request,'Task Has Been Deleted!')
	return redirect('todoview')

def edit(request,task_id):
	if request.method == 'POST':
		task = TodoModel.objects.get(pk=task_id)
		form = TodoModelForm(request.POST or None, instance = task)

		if form.is_valid():
			form.save()
			messages.success(request,'Task Has Been Edited!')
		return redirect('todoview')
	else:
		task = TodoModel.objects.get(pk=task_id)
		context = {'task': task}
		return render(request, 'edit.html', context)

	
	
	

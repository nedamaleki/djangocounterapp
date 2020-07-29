# Author: Neda Maleki
from django.shortcuts import render, redirect
from .models import Counter
# from django.http import HttpResponseRedirect

def helloworld (request):
	obj = Counter.objects.filter(id=1)[0]

	ournumber = obj.number
	context={'number': ournumber}
	return render(request, 'helloworld.html', context)

def hellostudent (request):
	name="neda"
	context={'name':name}
	return render(request, 'hellostudent.html', context)

def increment (request):
	obj = Counter.objects.get(pk=1)
	obj.number = int(obj.number)+1
	obj.save()
	return redirect('helloworld')
	
def decrement (request):
	obj= Counter.objects.filter(id=1)[0]
	obj.number = int(obj.number)-1
	obj.save()
	return redirect(request.META['HTTP_REFERER'])

def reset (request):
	obj= Counter.objects.filter(id=1)[0]
	obj.number = 0
	obj.save()
	return redirect('helloworld')


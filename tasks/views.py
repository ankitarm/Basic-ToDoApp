from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.


def list(request):
	tasks = List.objects.all()
	form = ListForm()
	if request.method == 'POST':
		form = ListForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect("/")
	content = {"tasks":tasks, "form":form}
	
	return render(request, "tasks/list.html", content)


def update(request, pk):
	tasks = List.objects.get(id=pk)
	form = ListForm(instance=tasks)
	if request.method == "POST":
		form = ListForm(request.POST, instance=tasks)
		if form.is_valid():
			form.save()
		return redirect("/")
	content = {"tasks":tasks, "form":form}
	
	return render(request, "tasks/update.html", content)


def delete(request, pk):
	tasks = List.objects.get(id=pk)

	if request.method == 'POST':
		tasks.delete()
		return redirect("/")
	content = {"tasks":tasks}
	
	return render(request, "tasks/delete.html", content)
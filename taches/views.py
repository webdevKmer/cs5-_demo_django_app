from django.shortcuts import redirect, render
from .forms import AddTaskForm
# Create your views here.

def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    context = {
        "tasks" : request.session["tasks"]
    }
    return render(request, 'taches/index.html', context)

def add_task(request):
    context = {
        "form" : AddTaskForm()
    }
    if (request.method == 'POST'):
        form = AddTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return redirect("taches_index")
        else:
            return render(request, 'taches/add_task.html', context)    
    return render(request, 'taches/add_task.html', context)
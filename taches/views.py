from django.shortcuts import redirect, render

# Create your views here.

tasks = ["chier","pisser","aller dormir","manger",]

def index(request):
    context = {
        "tasks" : tasks
    }
    return render(request, 'taches/index.html', context)

def add_task(request):
    if (request.method == 'POST'):
        task = request.POST["task"]
        tasks.append(task)
        return redirect("taches_index")
    task = "bouger"
    context = {
        "task" : task
    }
    return render(request, 'taches/add_task.html', context)
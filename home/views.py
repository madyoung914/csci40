from django.shortcuts import render

# Create your views here.
#this is new
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello world')

#new lesson

def task_list(request):
    ctx = {
        "tasks": [
            'Task 1',
            'Task 2',
            'Task 3',
            'Task 4',
            'Task 5'
        ]
    }
    return render(request, 'task_list.html', ctx)



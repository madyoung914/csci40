from django.urls import path

from .views import index, task_list

urlpatterns = [
    #the url, function name, name for a specific url
    path('', index, name='index'),
    path('task-list', task_list, name='task-list') 
]

app_name = "home"


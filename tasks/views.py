from django.core.exceptions import SuspiciousOperation
from django.http import Http404, HttpResponse
from django.shortcuts import render

from tasks.serializers import TaskSerializer
from .models import Task

from .forms import TaskForm


def task_list(request):
    if request.method == 'POST':
        serializer = TaskSerializer(data=request.POST)
        if serializer.is_valid():
            task = Task.objects.create(user=request.user, **serializer.data)
        else:
            raise SuspiciousOperation('Invalid Data')

    form = TaskForm()
    query = dict(request.GET.items())
    tasks = Task.objects.filter(user=request.user, **query)
    serializer = TaskSerializer(tasks, many=True)
    context = {'tasks_list': serializer.data, 'form': form}
    return render(request, 'tasks/task_list.html', context)


def task(request, pk):
    if request.method == 'GET':
        try:
            task = Task.objects.get(pk=pk, user=request.user)
        except Task.DoesNotExist:
            raise Http404()
        serializer = TaskSerializer(task)
        form = TaskForm(request.POST or None, initial={'title':task.title, 'description':task.description, 'deadline':task.deadline, 'status':task.status, 'priority':task.priority})
        return render(request, 'tasks/task.html', {'form': form, 'task_id': task.id,})


    if request.method == 'POST':
        try:
            task = Task.objects.filter(pk=pk, user=request.user)
        except Task.DoesNotExist:
            raise Http404()
        serializer = TaskSerializer(data=request.POST)
        if serializer.is_valid():
            task.update(**serializer.data)
        form = TaskForm(request.POST or None)#, initial={'title':task.title, 'description':task.description, 'deadline':task.deadline, 'status':task.status, 'priority':task.priority})
        return render(request, 'tasks/task.html', {'form': form, 'task_id': pk,})


def pending(request):
    form = TaskForm()
    query = dict(request.GET.items())
    pending = Task.objects.filter(user=request.user, status=Task.PENDING,**query)
    serializer = TaskSerializer(pending, many=True)
    context = {'tasks_list': serializer.data, 'form': form}
    return render(request, 'tasks/task_list.html', context)

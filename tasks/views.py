from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render

from rest_framework import status, viewsets
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response

from tasks.serializers import TaskSerializer
from tasks.models import Task


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


    def list(self, request):
        query = dict(self.request.GET.items())
        tasks = Task.objects.filter(user=self.request.user, **query)
        serializer = self.get_serializer(tasks, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            tasks = Task.objects.get(pk=pk, user=self.request.user)
        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(tasks)
        return Response(serializer.data)

    def create(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        try:
            tasks = Task.objects.get(pk=pk, user=self.request.user)
        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)        
        return super(viewsets.ModelViewSet, self).partial_update(request, pk)


    @list_route()
    def pending(self, request):
        query = dict(self.request.GET.items())
        pending = Task.objects.filter(user=self.request.user, status=Task.PENDING,**query)
        serializer = self.get_serializer(pending, many=True)
        return Response(serializer.data)
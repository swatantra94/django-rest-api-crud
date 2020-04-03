from django.shortcuts import render
from .models import Question,Choice
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from .serializers import TaskSerializer
from .models import Task


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list':latest_question_list}
    return render(request, 'polls/index.html')


@api_view(['GET'])
def apioverview(request):
    api_urls = {
    'List':'/task-list/',
    'Detail View':'/task-detail/<str:pk>/',
    'Create':'/task-create/',
    'Update':'/task-update/<str:pk>/',
    'Delete':'/task-delete/<str:pk>/',
    }

    return Response(api_urls)

@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def taskDetail(request, pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializer(tasks,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def taskCreate(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response("Error")
    return Response(serializer.data)

@api_view(['GET'])
def taskUpdate(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response("Error")
    return Response(serializer.data)

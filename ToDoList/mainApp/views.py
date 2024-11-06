from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *
# Create your views here.

class ListToDo(generics.ListAPIView):          #Read
    queryset=ToDo.objects.all()
    serializer_class=ToDoSerializer

class DetailTodo(generics.RetrieveUpdateAPIView):  #Update
    queryset = ToDo.objects.all()
    serializer_class=ToDoSerializer

class CreateTodo(generics.CreateAPIView):      #Create
    queryset= ToDo.objects.all()
    serializer_class=ToDoSerializer

class DeleteToDo(generics.DestroyAPIView):  #Delete
    queryset = ToDo.objects.all()
    serializer_class=ToDoSerializer
    
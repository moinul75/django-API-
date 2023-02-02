from django.shortcuts import render

from .serilizers import * 
from .models import * 
from rest_framework import generics


# Create your views here.
class todoList(generics.ListAPIView): #Read 
    queryset = Todo.objects.all()
    serializer_class = ToDoSerializer
    
class DetailsTodo(generics.RetrieveUpdateAPIView): #Update 
    queryset = Todo.objects.all()
    serializer_class = ToDoSerializer
    
class CreateTodo(generics.CreateAPIView): #Create 
    queryset = Todo.objects.all()
    serializer_class = ToDoSerializer
    
    
class DeleteTodo(generics.DestroyAPIView): #Delete 
    queryset = Todo.objects.all()
    serializer_class = ToDoSerializer
    






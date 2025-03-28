from django.shortcuts import render
from rest_framework import viewsets
from app.models import Todo
from app.serializer import TodoSerializer


class TodoViewset(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

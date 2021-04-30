from django.views import View
from django.views import generic
from rest_framework import viewsets
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Todo, Comment
from .serializers import TodoSerializer, TodoDetailSerializer, CommentSerializer


class TodoIndex(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class TodoMain(ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class TodoDetail(RetrieveAPIView):
    lookup_field = 'id'
    queryset = Todo.objects.all()
    serializer_class = TodoDetailSerializer

class CommentIndex(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


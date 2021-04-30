from django.views import View
from django.views import generic
from rest_framework import viewsets
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Todo_list, Comment
from .serializers import TodoSerializer, TodoDetailSerializer, CommentSerializer


class TodoIndex(viewsets.ModelViewSet):
    queryset = Todo_list.objects.all()
    serializer_class = TodoSerializer

class TodoMain(ListAPIView):
    queryset = Todo_list.objects.all().order_by('-created_at')
    serializer_class = TodoSerializer

class TodoDetail(RetrieveAPIView):
    lookup_field = 'id'
    queryset = Todo_list.objects.all()
    serializer_class = TodoDetailSerializer

class CommentIndex(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer

from rest_framework import viewsets
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from .models import TodoList, Comment
from .serializers import TodoSerializer, TodoDetailSerializer, CommentSerializer


class TodoIndex(viewsets.ModelViewSet):
    queryset = TodoList.objects.all()
    serializer_class = TodoSerializer

class TodoMain(ListAPIView):
    queryset = TodoList.objects.all().order_by('-created_at')
    serializer_class = TodoSerializer

class TodoDetail(RetrieveAPIView):
    lookup_field = 'id'
    queryset = TodoList.objects.all()
    serializer_class = TodoDetailSerializer

class CommentIndex(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer

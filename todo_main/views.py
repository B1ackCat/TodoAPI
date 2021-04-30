from django.views import View
from django.views import generic
from rest_framework import viewsets
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from .models import Todo_list, Comment
from .serializers import Todo_Serializer, Todo_Detail_Serializer, Comment_Serializer


class Todo_index(viewsets.ModelViewSet):
    queryset = Todo_list.objects.all()
    serializer_class = Todo_Serializer

class Todo_main(ListAPIView):
    queryset = Todo_list.objects.all().order_by('-created_at')
    serializer_class = Todo_Serializer

class Todo_detail(RetrieveAPIView):
    lookup_field = 'id'
    queryset = Todo_list.objects.all()
    serializer_class = Todo_Detail_Serializer

class Comment_index(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = Comment_Serializer

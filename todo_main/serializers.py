from .models import Todo_list, Comment
from rest_framework import serializers

class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Todo_list
        fields = ('id', 'title', 'description','is_completed','created_at','updated_at')

class TodoDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Todo_list
        fields = ('title', 'description', 'is_completed', 'updated_at')

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'contents', 'created_at', 'updated_at')

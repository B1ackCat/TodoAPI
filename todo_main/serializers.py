from .models import Todo_list, Comment
from rest_framework import serializers

class Todo_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Todo_list
        fields = ('id', 'title', 'description','is_completed','created_at','updated_at')

class Todo_Detail_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Todo_list
        fields = ('title', 'description', 'is_completed', 'updated_at')

class Comment_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'contents', 'created_at', 'updated_at')
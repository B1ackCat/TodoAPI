from django.db import models

class TodoList(models.Model):
    id = models.AutoField(db_column='ID', primary_key = True)
    title = models.CharField(db_column='TITLE', max_length=200)
    is_completed = models.BooleanField(db_column='IS_COMPLETED')
    description = models.TextField(db_column='DESCRIPTION', max_length=1000)
    created_at = models.DateField(db_column='CREATED_AT',auto_now_add=True)
    updated_at = models.DateField(db_column='UPDATED_AT', auto_now=True)

    class Meta:
        managed = False
        db_table = 'todo_list'

class Comment(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    contents = models.TextField(db_column='CONTENTS', max_length=500)
    created_at = models.DateField(db_column='CREATED_AT',auto_now_add=True)
    updated_at = models.DateField(db_column='UPDATED_AT', auto_now=True)

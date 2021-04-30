from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo_main.urls')),
    path('todos/', include('todo_main.urls')),
]

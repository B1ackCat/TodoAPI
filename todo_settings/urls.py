from django.contrib import admin
from django.urls import path
from django.conf.urls import include

from todo_main.documents_urls import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo_main.urls')),

    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^docs/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls import url, include
from django.urls import path
from rest_framework.permissions import AllowAny


schema_view = get_schema_view(
    openapi.Info(
        title = "Todo Open API",
        default_version= "version_0.1",
        description = "Todo Open API 문서 페이지 입니다.",
    ),
    validators=['flex'],
    public = True,
    permission_classes=(AllowAny,),
)


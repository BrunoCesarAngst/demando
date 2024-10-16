# /home/bruno/demando/demando/urls.py

from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

schema_view = get_schema_view(
    openapi.Info(
        title="Demando API",
        default_version='v1',
        description="Documentação da API para o Gerenciador de Demandas e Tarefas",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="bruno.angst@rede.ulbra.br"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('demandas/', include('demandas.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('', lambda request: redirect('lista_demandas'), name='home'),
]



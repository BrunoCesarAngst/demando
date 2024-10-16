# /home/bruno/demando/demandas/urls.py

from django.urls import include, path
from .views import adicionar_demanda, editar_todas_demandas, lista_demandas, cadastro_view, login_view, logout_view, marcar_concluido, editar_demanda
from rest_framework.routers import DefaultRouter
from .views import DemandaViewSet

roteador = DefaultRouter()
roteador.register(r'demandas', DemandaViewSet)

urlpatterns = [
    path('', lista_demandas, name='lista_demandas'),
    path('cadastro/', cadastro_view, name='cadastro'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('api/', include(roteador.urls)),
    path('<int:demanda_id>/editar/', editar_demanda, name='editar_demanda'),
    path('editar-todas/', editar_todas_demandas, name='editar_todas_demandas'),
    path('adicionar/', adicionar_demanda, name='adicionar_demanda'),
    path('<int:demanda_id>/concluir/', marcar_concluido, name='marcar_concluido'),
]

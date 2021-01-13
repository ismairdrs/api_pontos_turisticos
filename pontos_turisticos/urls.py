from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from apps.atracoes.api.viewsets import AtracaoViewSet
from apps.avaliacoes.api.viewsets import AvaliacaoViewSet
from apps.comentarios.api.viewsets import ComentarioViewSet
from apps.core.api.viewsets import PontoTuristicoViewSet
from apps.enderecos.api.viewsets import EnderecoViewSet

router = routers.DefaultRouter()
router.register('ponto_turisticos', PontoTuristicoViewSet, basename='PontoTuristico')
router.register('atracoes', AtracaoViewSet, basename='Atracao')
router.register('avaliacoes', AvaliacaoViewSet, basename='Avaliacao')
router.register('comentarios', ComentarioViewSet, basename='Comentario')
router.register('enderecos', EnderecoViewSet, basename='Endereco')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

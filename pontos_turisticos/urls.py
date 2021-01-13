from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from apps.atracoes.api.viewsets import AtracaoViewSet
from apps.avaliacoes.api.viewsets import AvaliacaoViewSet
from apps.comentarios.api.viewsets import ComentarioViewSet
from apps.core.api.viewsets import PontoTuristicoViewSet
from apps.enderecos.api.viewsets import EnderecoViewSet

router = routers.DefaultRouter()
router.register('ponto_turistico', PontoTuristicoViewSet)
router.register('atracoes', AtracaoViewSet)
router.register('avaliacoes', AvaliacaoViewSet)
router.register('comentario', ComentarioViewSet)
router.register('ponto_turistico', PontoTuristicoViewSet)
router.register('endereco', EnderecoViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

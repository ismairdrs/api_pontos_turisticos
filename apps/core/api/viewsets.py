from rest_framework import viewsets
from rest_framework.decorators import action

from apps.core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer


class PontoTuristicoViewSet(viewsets.ModelViewSet):
    # queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer

    def get_queryset(self):
        return PontoTuristico.objects.filter(aprovado=True)

    # list é o get do endpoint, retorna todos os objetos de pontos turisticos
    def list(self, request, *args, **kwargs):
        # é possível fazer validações e utilizar o super da classe
        return super(PontoTuristicoViewSet, self).list(request, *args, **kwargs)

    # create é o método que cria o objeto, é possível fazer as validaçõs de depois chamar o super
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        print(serializer)
        return super(PontoTuristicoViewSet, self).create(request, *args, **kwargs)

    # destroy é o método delete, são feitas muitas validações para esse método
    # usuário tem permissão para excluir, salvar log do usuário que excluiu
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        print(instance)
        return super(PontoTuristicoViewSet, self).destroy(request, *args, **kwargs)

    # esse é o método get de um único objeto (detail)
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        print(instance)
        return super(PontoTuristicoViewSet, self).retrieve(request, *args, **kwargs)

    # atualiza um objeto inteiro, dentro do self.data estão todos os dados necessários
    def update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).update(request, *args, **kwargs)

    # o partial_update é para atualizar parte do objeto, 1, 2 campos...
    def partial_update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).partial_update(request, *args, **kwargs)

    # o decorador @action permite criar novas actions na api
    # o methods diz como deve receber essa request
    # defail=True é para ele enviar a pk e conseguir acessar o objeto
    @action(methods=['get'], detail=True)
    def denunciar(self, request, pk=None):
        pass

    # essa é uma nova action do endpoint
    @action(methods=['get'], detail=False)
    def teste(self, request):
        pass

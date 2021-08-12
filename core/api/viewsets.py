from rest_framework import filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core.api.serializers import PontoTuristicoSerializer
from core.models import PontoTuristico

class PontoTuristicoViewSet(ModelViewSet):

#    queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nome', 'descricao', 'endereco__linha1']
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    lookup_field = 'nome' #fazendo getOne com nome (dá problema com objetos com mesmo nome, por isso o campo precisa ser único)

    def get_queryset(self):
        #Posso fazer multiplas filtragens dentro dessa lista e retornar ela :)
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)
        queryset = PontoTuristico.objects.all()

        if id:
            queryset = PontoTuristico.objects.filter(pk=id)
        if nome:
            queryset.filter(nome_iexact=nome)#lower
        if descricao:
            queryset.filter(descricao_iexact=descricao)

        return queryset

    #sobrescrevendo o método list abaixo, consigo filtrar o GET endpoint
    def list(self, request, *args, **kwargs):
        #return Response({'teste':123})
        return super(PontoTuristicoViewSet, self).list(request, *args, **kwargs)

    #sobrescrevendo o método abaixo eu consigo interceptar o post do cliente
    def create(self, request, *args, **kwargs):
        #return Response({'Hello': request.data['nome']})
        return super(PontoTuristicoViewSet, self).create(request, *args, **kwargs)

    #interceptando método delete
    def destroy(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).destroy(request, *args, **kwargs)

    #interceptando o método getOne do cliente
    def retrieve(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).retrieve(request, *args, **kwargs)

    #interceptando PUT
    def update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).update(request, *args, **kwargs)

    #interceptando o PATCH
    def partial_update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).partial_update(request, *args, **kwargs)

    # #criando minhas próprias actions
    # @action(methods=['get'], detail=True)#detail indica que é necessário a PK
    # def denunciar(self, request, pk=None):
    #     print("teste")
    #     return Response({"Teste": "chegou"})
    #
    # #criando minhas próprias actions (dessa vez sem PK)
    # @action(methods=['get'], detail=False)  # detail indica que é necessário a PK
    # def teste(self, request):
    #     print("teste")
    #     return Response({"Teste": "chegou sem pk"})
    #

from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from core.models import PontoTuristico
from atracoes.api.serializers import AtracoesSerializer
from endereco.api.serializers import EnderecoSerializer

class PontoTuristicoSerializer(ModelSerializer):
    atracoes = AtracoesSerializer(many=True)#Nested relationships #o many é para muitos
    endereco = EnderecoSerializer()#Nested relationships
    descricao_completa = SerializerMethodField()

    class Meta:
        model = PontoTuristico
        fields = ['id', 'nome', 'descricao', 'aprovado', 'foto', 'atracoes', 'comentarios', 'avaliacoes', 'endereco', 'descricao_completa', 'descricao_completa2']


    def get_descricao_completa(self, obj):
        return '%s - %s' % (obj.nome, obj.descricao)
from rest_framework import serializers
from grades.models import Prova
from grades.models import Gabarito
from grades.models import Aluno
from grades.models import GabaritoAluno

class ProvaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prova
        fields = ['id', 'materia', 'questao', 'resposta', 'created_at', 'updated_at']


class GabaritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gabarito
        fields = ['id', 'id_prova', 'questao', 'resposta', 'created_at', 'updated_at']

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome_completo', 'nota', 'status', 'id_prova', 'created_at', 'updated_at']


class GabaritoAlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GabaritoAluno
        fields = ['id', 'id_aluno', 'id_prova', 'questao', 'resposta', 'created_at', 'updated_at']
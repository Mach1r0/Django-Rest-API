from rest_framework import serializers 
from escola.models import Aluno, Curso

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno 
        field =  ['id', 'nome', 'rg', 'cpf']

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        field = '__all__'
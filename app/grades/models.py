from django.db import models

# Create your models here.
from django.db import models

class Questao(models)

class Prova(models.Model):
    materia     = models.CharField(max_length=30)
    questao     = models.CharField(max_length=30)
    resposta    = models.CharField(max_length=30)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.materia

class Gabarito(models.Model):
    id_prova    = models.ForeignKey(Prova, on_delete=models.CASCADE)
    questao     = models.CharField(max_length=30)
    resposta    = models.CharField(max_length=30)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.questao

class Aluno(models.Model):
    nome_completo = models.CharField(max_length=30)
    nota          = models.CharField(max_length=30)
    status        = models.CharField(max_length=30)
    id_prova      = models.ForeignKey(Prova, on_delete=models.CASCADE)
    created_at    = models.DateTimeField(auto_now_add=True)
    updated_at    = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome_completo


class GabaritoAluno(models.Model):
    id_aluno   = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    id_prova   = models.ForeignKey(Prova, on_delete=models.CASCADE)
    questao    = models.CharField(max_length=30)
    resposta   = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.resposta



    # def __str__(self):
    #     return self.full_name
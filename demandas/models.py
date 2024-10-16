from django.db import models
from django.contrib.auth.models import User

class Demanda(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    concluido = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo
    

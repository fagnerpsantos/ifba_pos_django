from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models

# Create your models here.

class Chave(models.Model):
    STATUS_CHOICES = [
        (1, "Disponível"),
        (2, "Indisponível"),
    ]
    nome = models.CharField(max_length=30, null=False, blank=False)
    descricao = models.CharField(max_length=100, null=False, blank=False)
    observacoes = models.TextField(null=False, blank=False)
    status = models.IntegerField(choices=STATUS_CHOICES, null=False, blank=False)

    def __str__(self):
        return self.nome
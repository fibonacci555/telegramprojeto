from django.db import models

# Create your models here.



class Contact(models.Model):
    nome = models.CharField(max_length=200, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    assunto = models.CharField(max_length=300, blank=False, null=False)
    body = models.TextField(max_length=1200, null=False, blank=False)

    def __str__(self):
        return f'Nome: {self.nome} | Assunto: {self.assunto} | Email: {self.email}'


class Inscricoes(models.Model):
    nome = models.CharField(max_length=200, blank=False, null=False)
    email = models.EmailField(blank=False, null=False, unique=True)
    phone = models.CharField(max_length=20, blank=False, null=False,unique=True)

    def __str__(self):
        return f'Nome: {self.nome} | Número: {self.phone} | Email: {self.email}'
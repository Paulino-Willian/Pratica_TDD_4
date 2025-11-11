from django.db import models
from django.conf import settings

class Agenda(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='contacts'
    )
    nome_completo = models.CharField('Nome', max_length=150)
    phone = models.CharField('Telefone', max_length=20, blank=True, null=True)
    email = models.EmailField('E-mail', blank=True, null=True)
    observacao = models.TextField('Observações', blank=True, null=True)

    class Meta:
        ordering = ['nome_completo']
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'

    def __str__(self):
        return f"{self.nome_completo} - {self.email}"

from django.db import models

class Banco(models.Model):
    id_compensacao = models.AutoField(primary_key=True)
    nome_instituicao = models.CharField(max_length=100)

    class Meta:
        db_table = 'bancos'

    def __str__(self):
        return self.nome_instituicao
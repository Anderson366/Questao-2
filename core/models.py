from django.db import models

# Create your models here.
class Curso(models.Model):
    nome = models.CharField(max_length=100)
    carga_horaria = models.IntegerField()
    ementa = models.CharField(max_length=100)
    valor = models.FloatField()

    def __str__(self):
        return self.nome

class Professor(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=50)
    valor_hora_aula = models.DecimalField(decimal_places=2, max_digits=6)
    class Meta:
        verbose_name_plural = 'Professores'
    def __str__(self):
        return self.nome

class Turma(models.Model):
    data_inicio = models.DateField()
    data_termino = models.DateField()
    hora_inicio = models.TimeField()
    hora_termino = models.TimeField()
    adm = models.ForeignKey(Curso, on_delete=models.CASCADE)
    adm1 = models.ForeignKey(Professor, on_delete=models.CASCADE)
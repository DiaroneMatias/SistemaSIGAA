from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 



# Create your models here.
             
class Aluno(models.Model):
    situacao_opcoes = (
        ('1', 'Matriculado'),
        ('2', 'Trancado'),
        ('3', 'Cancelado'),
    )
    
    nome = models.CharField('Nome', max_length=250)
    cpf = models.CharField('CPF', max_length=11)
    matricula = models.CharField('Matrícula', max_length=10)
    idade = models.PositiveSmallIntegerField('Idade', default=0)
    nasc = models.DateTimeField('Data de Nascimento')
    #foto = models.ImageField()
    situacao = models.CharField('Situação', max_length=10, choices=situacao_opcoes, default='2')    
    observacoes = models.TextField('Observações')
    cadastro = models.DateTimeField('Cadastro', auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now_add=True)
    mediaGeral = models.PositiveSmallIntegerField('Média Geral', default=0)
    def __str__(self):
        return str(self.nome)
    
class Curso(models.Model):
    nome = models.CharField('Nome do Curso', max_length=120)
    totalCreditos = models.CharField('Total de Créditos', max_length=4)
    coordenador = models.CharField(max_length=120)   
    def __str__(self):
        return  str(self.nome) 
            
class PeriodoLetivo(models.Model):
    ano = models.CharField(max_length=4)
    semestre = models.CharField(max_length=10)
    dataInicio = models.DateField('Data de Início')
    dataFim = models.DateField('Data de Término')
    def __str__(self):
        return  str(self.semestre)
    
class Disciplina(models.Model):
    nome = models.CharField('Nome da Disciplina', max_length=120)
    creditos = models.CharField('Créditos', max_length=2)
    limiteFalta = models.CharField('Limite de Faltas', max_length=3)
    def __str__(self):
        return  str(self.nome)
           
class Turma(models.Model):
    ano = models.CharField(max_length=4)
    semestre = models.DateField(null= True, blank=True)
    disciplina = models.CharField(max_length=120)
    numeroVagas = models.CharField('Número de Vagas', max_length=3)
    professor = models.CharField(max_length=50)
    def __str__(self):
        return  str(self.ano)
        
class Professor(models.Model):
    nome = models.CharField(max_length=120)
    matricula = models.CharField('Matrícula', max_length=10)
    def __str__(self):
        return  str(self.nome)
            
class Matricula(models.Model):
    ano = models.CharField(max_length=4)
    semestre = models.CharField(max_length=10) 
    matriculaAluno = models.CharField('Matrícula do Aluno', max_length=10)
    codDisciplina = models.CharField('Código da Disciplina', max_length=10)
    nota1 = models.CharField('Nota 1', max_length=4)
    nota2 = models.CharField('Nota 2', max_length=4)
    falta1 = models.CharField('Falta 1', max_length=4)
    falta2 = models.CharField('Falta 2', max_length=4)
    def __str__(self):
        return  str(self.matriculaAluno)
    
class Historico(models.Model):
    situacao_opcoes = (
        ('1', 'Aprovado'),
        ('2', 'Reprovado'),
    )
    nome = models.CharField('Nome do Aluno', max_length=250)
    totalCreditos = models.CharField('Total de Créditos', max_length=10) 
    curso = models.CharField('Nome do Curso', max_length=10)
    disciplina = models.CharField('Disciplina Cursada', max_length=120)
    mediaDisciplina = models.PositiveSmallIntegerField('Média da Disciplina', default=0)
    nota1 = models.PositiveSmallIntegerField('Nota Primerio Semestre', default=0)
    nota2 = models.PositiveSmallIntegerField('Nota Segundo Semestre', default=0)
    mediaGeral = models.PositiveSmallIntegerField('Média Geral do Aluno', default=0)
    situacao = models.CharField('Situação', max_length=10, choices=situacao_opcoes, default='1')
    def __str__(self):
        return  str(self.nome)
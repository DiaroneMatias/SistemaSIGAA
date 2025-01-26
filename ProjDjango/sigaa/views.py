from django.shortcuts import render, redirect
from .models import Aluno
import sigaa
from sigaa.models import Aluno
from sigaa.models import Curso
from sigaa.models import Professor
from sigaa.models import PeriodoLetivo
from sigaa.models import Disciplina
from sigaa.models import Turma
from sigaa.models import Matricula
from sigaa.models import Historico
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/login/')
def logout_user(request):
    logout(request)
    return redirect('/login/')

def login_usuario(request):
    return render(request, 'login.html')

@csrf_protect
def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Usuário e Senha não conferem!')
    return redirect('/login/')



 # Defs de listagem -----------------------------------------------------------------------------------------
def aluno_listar(request):
    alunos = Aluno.objects.all().order_by('nome')
    return render(request, 'aluno/listarAluno.html', {'alunos': alunos})

def professor_listar(request):
    professores = Professor.objects.all().order_by('nome')
    return render(request, 'professor/listarProfessor.html', {'professores': professores})

def curso_listar(request):
    cursos = Curso.objects.all().order_by('nome')
    return render(request, 'curso/listarCurso.html', {'cursos': cursos})

def periodoLetivo_listar(request):
    periodos = PeriodoLetivo.objects.all().order_by('ano')
    return render(request, 'periodoLetivo/listarPeriodoLetivo.html', {'periodos': periodos})

def disciplina_listar(request):
    disciplinas = Disciplina.objects.all().order_by('nome')
    return render(request, 'disciplina/listarDisciplina.html', {'disciplinas': disciplinas})

def turma_listar(request):
    turmas = Turma.objects.all().order_by('ano')
    return render(request, 'turma/listarTurma.html', {'turmas': turmas})

def matricula_listar(request):
    matriculas = Matricula.objects.all().order_by('matriculaAluno')
    return render(request, 'matricula/listarMatricula.html', {'matriculas': matriculas})

def historico_listar(request):
    historicos = Matricula.objects.all().order_by('matriculaAluno')
    return render(request, 'historico/detalharHistorico.html', {'historicos': historicos})



 # Defs de detalhes ------------------------------------------------------------------------------------------ 
def aluno_detalhar(request, id):
    aluno = Aluno.objects.get(id=id)
    return render(request, 'aluno/detalharAluno.html', {'aluno': aluno})

def curso_detalhar(request, id):
    curso = Curso.objects.get(id=id)
    return render(request, 'curso/detalharCurso.html', {'curso': curso})

def professor_detalhar(request, id):
    professor = Professor.objects.get(id=id)
    return render(request, 'professor/detalharProfessor.html', {'professor': professor})

def periodoLetivo_detalhar(request, id):
    periodoLetivo = PeriodoLetivo.objects.get(id=id)
    return render(request, 'periodoLetivo/detalharPeriodoLetivo.html', {'periodoLetivo': periodoLetivo})

def disciplina_detalhar(request, id):
    disciplina = Disciplina.objects.get(id=id)
    return render(request, 'disciplina/detalharDisciplina.html', {'disciplina': disciplina})

def turma_detalhar(request, id):
    turma = Turma.objects.get(id=id)
    return render(request, 'turma/detalharTurma.html', {'turma': turma})

def matricula_detalhar(request, id):
    matricula = Matricula.objects.get(id=id)
    return render(request, 'matricula/detalharMatricula.html', {'matricula': matricula})

def historico_detalhar(request, id):
    historico = Historico.objects.get(id=id)
    return render(request, 'historico/detalharHistorico.html', {'historico': historico})
                  


 # Defs de registro ----------------------------------------------------------------------------------------
@login_required(login_url='/login/')
def aluno_registrar(request):
    aluno_id = request.GET.get('id')
    matricula = Matricula.objects.all()
    if aluno_id:
        aluno = Aluno.objects.get(id=aluno_id)
        return render(request, 'aluno/registrarAluno.html', {'aluno':aluno, 'matricula': matricula})
    return render(request, 'aluno/registrarAluno.html', {'matricula': matricula})

@login_required(login_url='/login/')
def aluno_set(request):
    nome = request.POST.get('nome')
    cpf = request.POST.get('cpf')
    matricula = request.POST.get('matricula')
    idade = request.POST.get('idade')
    nasc = request.POST.get('nasc')
    situacao = request.POST.get('situacao')
    observacoes = request.POST.get('observacoes')
    aluno_id = request.POST.get('aluno_id')
    if aluno_id:
        a = Aluno.objects.get(id=aluno_id)
        a.nome = nome
        a.cpf = cpf
        a.matricula = matricula
        a.idade = idade
        a.nasc = nasc
        a.situacao = situacao
        a.observacoes = observacoes
        a.save()
        url = '/aluno/detail/{}/'.format(aluno_id)
        return redirect(url)
    
    else:
        aluno = Aluno.objects.create(nome=nome, cpf=cpf, matricula=matricula, idade=idade, nasc=nasc, 
                                 situacao=situacao, observacoes=observacoes)   
    url = '/aluno/detail/{}/'.format(aluno.id)
    return redirect(url)

@login_required(login_url='/login/')
def curso_registrar(request):
    curso_id = request.GET.get('id')
    professor = Professor.objects.all()
    if curso_id:
        curso = Curso.objects.get(id=curso_id)
        return render(request, 'curso/registrarCurso.html', {'curso':curso, 'professor': professor})
    return render(request, 'curso/registrarCurso.html', {'professor': professor})

@login_required(login_url='/login/')
def curso_set(request):
    nome = request.POST.get('nome')
    totalCreditos = request.POST.get('totalCreditos')
    coordenador = request.POST.get('coordenador')
    curso_id = request.POST.get('curso_id')
    if curso_id:
        c = Curso.objects.get(id=curso_id)
        c.nome = nome
        c.totalCreditos = totalCreditos
        c.coordenador = coordenador
        c.save() 
        url = '/curso/detail/{}/'.format(curso_id)
        return redirect(url)  
    else:
        curso = Curso.objects.create(nome=nome, totalCreditos=totalCreditos, coordenador=coordenador)
    url = '/curso/detail/{}/'.format(curso.id)
    return redirect(url)

@login_required(login_url='/login/')
def matricula_registrar(request):
    matricula_id = request.GET.get('id')
    if matricula_id:
        matricula = Matricula.objects.get(id=matricula_id)
        return render(request, 'matricula/registrarMatricula.html', {'matricula': matricula})
    return render(request, 'matricula/registrarMatricula.html')

@login_required(login_url='/login/')
def matricula_set(request):
    ano = request.POST.get('ano')
    semestre = request.POST.get('semestre')
    matriculaAluno = request.POST.get('matriculaAluno')
    codDisciplina = request.POST.get('codDisciplina')
    nota1 = request.POST.get('nota1')
    nota2 = request.POST.get('nota2')
    falta1 = request.POST.get('falta1')
    falta2 = request.POST.get('falta2')
    matricula_id = request.POST.get('matricula_id')
    if matricula_id:
        m = Matricula.objects.get(id=matricula_id)
        m.ano = ano
        m.semestre = semestre
        m.matriculaAluno = matriculaAluno
        m.nota1 = nota1
        m.nota2 = nota2
        m.falta1 = falta1
        m.falta2 = falta2
        m.save()
        url = '/matricula/detail/{}/'.format(matricula_id)
        return redirect(url)
    else:
        matricula = Matricula.objects.create(ano=ano, semestre=semestre, matriculaAluno=matriculaAluno, 
                                         codDisciplina=codDisciplina, nota1=nota1, nota2=nota2, 
                                         falta1=falta1, falta2=falta2)
    url = '/matricula/detail/{}/'.format(matricula.id)
    return redirect(url)

@login_required(login_url='/login/')
def professor_registrar(request):
    professor_id = request.GET.get('id')
    if professor_id:
        professor = Professor.objects.get(id=professor_id)
        return render(request, 'professor/registrarProfessor.html', {'professor': professor})
    return render(request, 'professor/registrarProfessor.html')

@login_required(login_url='/login/')
def professor_set(request):
    nome = request.POST.get('nome')
    matricula = request.POST.get('matricula')
    professor_id = request.POST.get('professor_id')
    if professor_id:
        p = Professor.objects.get(id=professor_id)
        p.nome = nome
        p.matricula = matricula
        p.save() 
        url = '/professor/detail/{}/'.format(professor_id)
        return redirect(url)  
    else:
        professor = Professor.objects.create(nome=nome, matricula=matricula)
    url = '/professor/detail/{}/'.format(professor.id)
    return redirect(url)

@login_required(login_url='/login/')
def disciplina_registrar(request):
    disciplina_id = request.GET.get('id')
    if disciplina_id:
        disciplina = Disciplina.objects.get(id=disciplina_id)
        return render(request, 'disciplina/registrarDisciplina.html', {'disciplina': disciplina})
    return render(request, 'disciplina/registrarDisciplina.html')

@login_required(login_url='/login/')
def disciplina_set(request):
    nome = request.POST.get('nome')
    creditos = request.POST.get('creditos')
    limiteFalta = request.POST.get('limiteFalta')
    disciplina_id = request.POST.get('disciplina_id')
    if disciplina_id:
        d = Disciplina.objects.get(id=disciplina_id)
        d.nome = nome
        d.creditos = creditos
        d.limiteFalta = limiteFalta
        d.save()
        url = '/disciplina/detail/{}/'.format(disciplina_id)
        return redirect(url)
    else:
        disciplina = Disciplina.objects.create(nome=nome, creditos=creditos, limiteFalta=limiteFalta)
    url = '/disciplina/detail/{}/'.format(disciplina.id)
    return redirect(url)

@login_required(login_url='/login/')
def periodoLetivo_registrar(request):
    periodoLetivo_id = request.GET.get('id')
    if periodoLetivo_id:
        periodoLetivo = PeriodoLetivo.objects.get(id=periodoLetivo_id)
        return render(request, 'periodoLetivo/registrarPeriodoLetivo.html', {'periodoLetivo': periodoLetivo})
    return render(request, 'periodoLetivo/registrarPeriodoLetivo.html')

@login_required(login_url='/login/')
def periodoLetivo_set(request):
    ano = request.POST.get('ano')
    semestre = request.POST.get('semestre')
    dataInicio = request.POST.get('dataInicio')
    dataFim = request.POST.get('dataFim')
    periodoLetivo_id = request.POST.get('periodoLetivo_id')
    if periodoLetivo_id:
        pl = PeriodoLetivo.objects.get(id=periodoLetivo_id)
        pl.ano = ano
        pl.semestre = semestre
        pl.dataInicio = dataInicio
        pl.dataFim = dataFim
        pl.save()
        url = '/periodoLetivo/detail/{}/'.format(periodoLetivo_id)
        return redirect(url)
    else:
        periodoLetivo = PeriodoLetivo.objects.create(ano=ano, semestre=semestre, dataInicio=dataInicio, 
                                                 dataFim=dataFim)
    url = '/periodoLetivo/detail/{}/'.format(periodoLetivo.id)
    return redirect(url)

@login_required(login_url='/login/')
def turma_registrar(request):
    turma_id = request.GET.get('id')
    disciplina = Disciplina.objects.all()
    professor = Professor.objects.all()
    if turma_id:
        turma = Turma.objects.get(id=turma_id)
        return render(request, 'turma/registrarTurma.html', {'disciplina': disciplina, 'professor': professor})
    return render(request, 'turma/registrarTurma.html', {'disciplina': disciplina, 'professor': professor})

@login_required(login_url='/login/')
def turma_set(request):
    ano = request.POST.get('ano')
    semestre = request.POST.get('semestre')
    disciplina = request.POST.get('disciplina')
    numeroVagas = request.POST.get('numeroVagas')
    professor = request.POST.get('professor')
    turma_id = request.POST.get('turma_id')
    if turma_id:
        t = Turma.objects.get(id=turma_id)
        t.ano = ano
        t.semestre = semestre
        t.disciplina = disciplina
        t.numeroVagas = numeroVagas
        t.professor = professor
        t.save()
        url = '/turma/detail/{}/'.format(turma_id)
        return redirect(url)
    else:
        turma = Turma.objects.create(ano=ano, semestre=semestre, disciplina=disciplina, 
                                                 numeroVagas=numeroVagas, professor=professor)
    url = '/turma/detail/{}/'.format(turma.id)
    return redirect(url)



# Defs de deletar ----------------------------------------------------------------------------------------
@login_required(login_url='/login/')
def aluno_deletar(request, id):
    aluno = Aluno.objects.get(id=id)
    #if aluno.user == request.user:
    aluno.delete()
    return redirect('/aluno/all/')

@login_required(login_url='/login/')
def curso_deletar(request, id):
    curso = Curso.objects.get(id=id)
    #if aluno.user == request.user:
    curso.delete()
    return redirect('/curso/all/')

@login_required(login_url='/login/')
def matricula_deletar(request, id):
    matricula = Matricula.objects.get(id=id)
    #if aluno.user == request.user:
    matricula.delete()
    return redirect('/matricula/all/')

@login_required(login_url='/login/')
def professor_deletar(request, id):
    professor = Professor.objects.get(id=id)
    #if aluno.user == request.user:
    professor.delete()
    return redirect('/professor/all/')

@login_required(login_url='/login/')
def disciplina_deletar(request, id):
    disciplina = Disciplina.objects.get(id=id)
    #if aluno.user == request.user:
    disciplina.delete()
    return redirect('/disciplina/all/')

@login_required(login_url='/login/')
def periodoLetivo_deletar(request, id):
    periodoLetivo = PeriodoLetivo.objects.get(id=id)
    #if aluno.user == request.user:
    periodoLetivo.delete()
    return redirect('/periodoLetivo/all/')

@login_required(login_url='/login/')
def turma_deletar(request, id):
    turma = Turma.objects.get(id=id)
    #if aluno.user == request.user:
    turma.delete()
    return redirect('/turma/all/')
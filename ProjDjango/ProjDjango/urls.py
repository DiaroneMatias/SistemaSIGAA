"""ProjDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from sigaa import views
from django.views.generic import RedirectView
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from . import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_usuario),
    path('login/submit', views.submit_login),
    path('logout/', views.logout_user),
    path('', RedirectView.as_view(url='aluno/all/')),
    
    # Listagem dos Objetos ----------------------------------------------------------------------------
    path('aluno/all/', views.aluno_listar),
    path('curso/all/', views.curso_listar),
    path('professor/all/', views.professor_listar),
    path('periodoLetivo/all/', views.periodoLetivo_listar),
    path('disciplina/all/', views.disciplina_listar),
    path('turma/all/', views.turma_listar),
    path('matricula/all/', views.matricula_listar),
    
    # Detalhes dos Objetos --------------------------------------------------------------------------------
    path('aluno/detail/<id>/', views.aluno_detalhar),
    path('curso/detail/<id>/', views.curso_detalhar),
    path('professor/detail/<id>/', views.professor_detalhar),
    path('periodoLetivo/detail/<id>/', views.periodoLetivo_detalhar),
    path('disciplina/detail/<id>/', views.disciplina_detalhar),
    path('turma/detail/<id>/', views.turma_detalhar),
    path('matricula/detail/<id>/', views.matricula_detalhar),
    path('historico/detail/<id>/', views.historico_detalhar),
    
    # Registrar Objetos -------------------------------------------------------------------------------------
    path('aluno/register/', views.aluno_registrar),
    path('aluno/register/submit', views.aluno_set),
    path('curso/register/', views.curso_registrar),
    path('curso/register/submit', views.curso_set),
    path('matricula/register/', views.matricula_registrar),
    path('matricula/register/submit', views.matricula_set),
    path('professor/register/', views.professor_registrar),
    path('professor/register/submit', views.professor_set),
    path('disciplina/register/', views.disciplina_registrar),
    path('disciplina/register/submit', views.disciplina_set),
    path('periodoLetivo/register/', views.periodoLetivo_registrar),
    path('periodoLetivo/register/submit', views.periodoLetivo_set),
    path('turma/register/', views.turma_registrar),
    path('turma/register/submit', views.turma_set),
    
    # Deletar Objetos -------------------------------------------------------------------------------------
    path('aluno/deletar/<id>/', views.aluno_deletar),
    path('curso/deletar/<id>/', views.curso_deletar),
    path('matricula/deletar/<id>/', views.matricula_deletar),
    path('professor/deletar/<id>/', views.professor_deletar),
    path('disciplina/deletar/<id>/', views.disciplina_deletar),
    path('periodoLetivo/deletar/<id>/', views.periodoLetivo_deletar),
    path('turma/deletar/<id>/', views.turma_deletar),
    
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
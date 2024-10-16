#/home/bruno/demando/demandas/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse

from .forms import DemandaForm
from .models import Demanda
from .serializadores import DemandaSerializador
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

# View para listar demandas
def lista_demandas(request):
    demandas_lista = Demanda.objects.all().order_by('-criado_em')  # Ordena pela data de criação
    paginator = Paginator(demandas_lista, 10)  # Paginação: 10 demandas por página
    page_number = request.GET.get('page')
    demandas = paginator.get_page(page_number)

    if request.headers.get('hx-request'):
        return render(request, 'demandas/fragmentos/lista_demandas.html', {'demandas': demandas})

    return render(request, 'demandas/lista_demandas.html', {'demandas': demandas})

# View para cadastro de novos usuários
def cadastro_view(request):
    if request.user.is_authenticated:
        return redirect('lista_demandas')  # Redireciona usuário autenticado
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastro realizado com sucesso! Agora você pode fazer login.')
            return redirect('login')
    else:
        form = UserCreationForm()
    
    return render(request, 'demandas/cadastro.html', {'form': form})

# View para editar uma demanda
def editar_demanda(request, demanda_id):
    demanda = get_object_or_404(Demanda, id=demanda_id)

    if request.method == 'POST':
        form = DemandaForm(request.POST, instance=demanda)
        if form.is_valid():
            form.save()
            return redirect('lista_demandas')
    else:
        form = DemandaForm(instance=demanda)

    return render(request, 'demandas/editar_demanda.html', {'form': form, 'demanda': demanda})

# View para editar todas as demandas (lista com links de edição)
def editar_todas_demandas(request):
    demandas = Demanda.objects.all()
    return render(request, 'demandas/editar_todas_demandas.html', {'demandas': demandas})

@csrf_exempt
@login_required
def adicionar_demanda(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        if titulo and descricao:
            demanda = Demanda.objects.create(
                titulo=titulo,
                descricao=descricao,
                usuario=request.user  # Associar o usuário autenticado à demanda
            )
            return render(request, 'demandas/fragmentos/demanda_item.html', {'demanda': demanda})
    return JsonResponse({'error': 'Dados inválidos'}, status=400)

# View para login de usuários
def login_view(request):
    if request.user.is_authenticated:
        return redirect('lista_demandas')  # Redireciona usuário autenticado
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('lista_demandas')
            else:
                messages.error(request, 'Usuário ou senha incorretos.')
        else:
            messages.error(request, 'Erro na autenticação.')
    else:
        form = AuthenticationForm()
    
    return render(request, 'demandas/login.html', {'form': form})

# View para logout de usuários
def logout_view(request):
    logout(request)
    return redirect('login')

# View para marcar demanda como concluída
@csrf_exempt
def marcar_concluido(request, demanda_id):
    demanda = get_object_or_404(Demanda, id=demanda_id)
    demanda.concluido = True
    demanda.save()
    return JsonResponse({'status': 'concluido'})

# ViewSet para a API de demandas
class DemandaViewSet(viewsets.ModelViewSet):
    queryset = Demanda.objects.all()
    serializer_class = DemandaSerializador
    permission_classes = [IsAuthenticated]  # Restrição de permissão: apenas usuários autenticados


from django.shortcuts import render, redirect
from .models import Especialidades, DadosMedico, is_medico
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.messages import constants



def cadastro_medico(request):
    
    if is_medico(request.user):
        messages.add_message(request, constants.WARNING, 'Você já está cadastrado como médico.')
        return redirect('/medicos/abrir_horarios')
    
    if request.method == "GET":
        especicalidades = Especialidades.objects.all()
        return render(request, 'cadastro_medico.html', { 'especialidades' : especicalidades })
    elif request.method == "POST":
        crm = request.POST.get('crm')
        nome = request.POST.get('nome')
        cep = request.POST.get('cep')
        rua = request.POST.get('rua')
        bairro = request.POST.get('bairro')
        numero = request.POST.get('numero')
        cim = request.FILES.get('cim')
        rg = request.FILES.get('rg')
        foto = request.FILES.get('foto')
        especialidade = request.POST.get('especialidade')
        decricao = request.POST.get('decricao')
        valor_consulta = request.POST.get('valor_consulta')
        
        dados_medico = DadosMedico(
            crm=crm,
            nome=nome,
            cep=cep,
            rua=rua,
            bairro=bairro,
            numero=numero,
            cedula_identidade_medica=cim,
            rg=rg,
            foto=foto,
            especialidade_id=especialidade,
            decricao=decricao,
            valor_consulta=valor_consulta,
            user=request.user
        )
        
        dados_medico.save()
        
        messages.add_message(request, constants.SUCCESS, 'Cadastro médico realizado com sucesso!')
        return  redirect('/medicos/abrir_horarios')
        

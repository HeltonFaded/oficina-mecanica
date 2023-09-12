from django.shortcuts import render, get_object_or_404
from .forms import FormServico
from django.http import HttpResponse,FileResponse
from .models import Servico,ServicoAdicional
from fpdf import FPDF
from io import BytesIO
from django.shortcuts import redirect
from django.contrib import messages
def novo_servico(request):
    if request.method == "GET":
        form = FormServico()
        return render(request, 'novo_servico.html', {'form': form})
    elif request.method == "POST":
        form = FormServico(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'novo serviço salvo com sucesso',extra_tags='success-message')
            return redirect('clientes')
        else:
            return render(request, 'novo_servico.html', {'form': form})

def listar_servico(request):
    if request.method == "GET":
        servicos = Servico.objects.all()
        return render(request, 'listar_servico.html', {'servicos': servicos})

def servico(request, identificador):
    servico = get_object_or_404(Servico, identificador=identificador)
    return render(request, 'servico.html', {'servico': servico})

def salvo_sucesso(request):
                messages.success(request, 'alterações salvas com sucesso!',extra_tags='success-message')
                return redirect('clientes')


def gerar_os (request, identificador):
    servico = get_object_or_404(Servico, identificador=identificador)

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 12)
    pdf.set_fill_color(240,240,240)
    pdf.cell(35, 10, 'cliente:',1,0,'L',1)
    pdf.cell(0, 10, f'- {servico.cliente.nome}',1,1,'L',1)
    pdf.cell(35,10, 'Manutenções:', 1, 0, 'L', 1)
    categorias_manutenção = servico.categoria_manutencao.all()
    for i,manutenção in enumerate(categorias_manutenção):
        pdf.cell(0, 10, f"- {manutenção.get_titulo_display()}", 1,1,'L',1)
        if not i == len(categorias_manutenção)-1:
            pdf.cell(35,10,'',0,0)

    pdf.cell(35,10,'ID:',1,0,"L",1)
    pdf.cell(0,10,f'- {servico.identificador}',1,1,"L",1)         
    
    pdf.cell(35,10,'Data de Início:',1,0,"L",1)
    pdf.cell(0,10,f'- {servico.data_inicio}',1,1,"L",1)

    pdf.cell(35,10,'Data de entrega:',1,0,"L",1)
    pdf.cell(0,10,f'- {servico.data_entrega}',1,1,"L",1)

    pdf.cell(35,10,'Protocolo:',1,0,"L",1)
    pdf.cell(0,10,f'- {servico.protocole}',1,1,"L",1)


    pdf.cell(35, 10, 'Valor:', 1, 0, "L", 1)
    pdf.cell(0, 10, f'- R${servico.preco_total()}', 1, 1, "L", 1)

    pdf_content = pdf.output(dest='S').encode('latin1')
    pdf_bytes = BytesIO(pdf_content)

    return FileResponse (pdf_bytes,as_attachment=True, filename=f'ordem de serviço protocolo : {servico.identificador}.pdf')

def servico_adicional(request):
    identificador_servico = request.POST.get('Identificador_servico')
    titulo = request.POST.get('titulo')
    preco = request.POST.get('preco')
    descricao = request.POST.get('descrição')

    servico_adicional = ServicoAdicional(titulo=titulo, descricao=descricao, PRECO=preco)

    servico_adicional.save()
    servico = Servico.objects.get(identificador=identificador_servico)
    servico.servicos_adicionais.add(servico_adicional)
    servico.save()
    messages.success(request, 'alterações salvas com sucesso!',extra_tags='success-message')
    return redirect('clientes')
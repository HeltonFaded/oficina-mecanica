from django.forms import ModelForm
from .models import Servico, CategoriaManutencao


class FormServico(ModelForm):
    class Meta:
        model = Servico
        exclude = ['finalizado', 'protocole','identificador','servicos_adicionais']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
            self.fields[field].widget.attrs.update({'placeholder': field})
        
        choices = []
        categorias = CategoriaManutencao.objects.filter(titulo__in=[j for i, j in self.fields['categoria_manutencao'].choices])
        for categoria in categorias:
            choices.append((categoria.pk, categoria.get_titulo_display()))

        self.fields['categoria_manutencao'].choices = choices

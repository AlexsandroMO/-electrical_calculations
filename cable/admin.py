
from django.contrib import admin
from .models import TabelaCondutor, TipoCircuito, Disjuntor, Tensao, Project, ResidencDimens


class ListaTabelaCondutor(admin.ModelAdmin):
    list_display = ('secao','capacidade_conducao','queda_tesao')


class ListaResidencDimens(admin.ModelAdmin):
    list_display = ('projeto','local','tipo','tensa_va','quant','potencia_va','comprimento',
                    'sessao_condutor','queda_tensao_ckt','queda_tensao_perm','queda_tensao_test','capacidade_corrente',
                    'numero_polos','corrente_nominal','verifica_dj')

class ListaProject(admin.ModelAdmin):
    list_display = ('project','description')
    

admin.site.register(TabelaCondutor, ListaTabelaCondutor)
admin.site.register(TipoCircuito)
admin.site.register(Disjuntor)
admin.site.register(Tensao)
admin.site.register(Project, ListaProject)
admin.site.register(ResidencDimens, ListaResidencDimens)


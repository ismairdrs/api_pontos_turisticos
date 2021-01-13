from django.contrib import admin
from .models import Atracao


class AtracoesAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'horario_funcionamento', 'idade_minima')


admin.site.register(Atracao, AtracoesAdmin)

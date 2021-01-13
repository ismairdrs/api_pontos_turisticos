from django.contrib import admin
from .models import Endereco


class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('linha1', 'linha2', 'cidade', 'estado', 'pais')


admin.site.register(Endereco, EnderecoAdmin)

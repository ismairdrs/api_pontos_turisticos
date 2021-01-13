from django.contrib import admin
from .models import PontoTuristico


class PontoTuristicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'aprovado', )


admin.site.register(PontoTuristico, PontoTuristicoAdmin)

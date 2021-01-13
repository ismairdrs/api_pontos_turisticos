from django.contrib import admin
from .models import Comentario


class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'comentario', 'aprovado',)


admin.site.register(Comentario, ComentarioAdmin)

"""blah blah."""
from django.contrib import admin

from boteco.models import Postagem, Comentario, Magote, Perfil, Bebida


class PerfilAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "foto_perfil",
        "qtd_chifres",
        "status",
        "ultimo_chifre",
        "procurando_mais",
    ]
    search_fields = ["user"]
    list_filter = ["status", "procurando_mais"]
    ordering = ["user"]


# Register your models here.
admin.site.register(Postagem)
admin.site.register(Perfil, PerfilAdmin)
admin.site.register(Comentario)
admin.site.register(Magote)
admin.site.register(Bebida)

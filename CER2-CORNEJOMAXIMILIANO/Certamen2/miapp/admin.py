from django.contrib import admin
from .models import Entidad, Comunicador
from django.core.exceptions import PermissionDenied

# Register your models here.
class comunicados(admin.ModelAdmin):
    list_display = ("titulo","id","tipo","fecha_publicacion","entidad","publicado_por")
    list_filter = [("publicado_por",admin.RelatedOnlyFieldListFilter),]



    def save_model(self, request, obj, form, change):
        if change:
            if ((request.user != obj.entidad.administrador) and (request.user.is_superuser == False)):
                raise PermissionDenied
        else:
            obj.publicado_por = request.user     
            for ent in Entidad.objects.all():
                if ent.administrador == request.user:
                    obj.entidad = ent
        super().save_model(request, obj, form, change)
    
    def delete_model(self, request, object):
        if ((request.user != object.entidad.administrador) and (request.user.is_superuser == False)):
            raise PermissionDenied
        else:
            object.delete()

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions


admin.site.register(Entidad)
admin.site.register(Comunicador,comunicados)



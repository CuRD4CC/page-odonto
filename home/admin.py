from django.contrib import admin
from usuarios.models import DatosExtra
from .models import Tratamiento

admin.site.register(DatosExtra)

class TratamientoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
admin.site.register(Tratamiento, TratamientoAdmin)
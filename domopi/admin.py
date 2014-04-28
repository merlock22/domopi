from django.contrib import admin
from domopi.models import *
# Register your models here.

class ComandoInline(admin.StackedInline):
    model = Comandos
    extra = 1

class DispositivoInline(admin.StackedInline):
    model = Dispositivo
    extra = 1
    exclude=('descripcion','tipo_disp','direccion','tipo_acceso',)

class DispositivoAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ('nombre','descripcion','tipo_disp','direccion','tipo_acceso','habitacion')}),                
    ]
    inlines = [ComandoInline]
    list_display = ('nombre', 'descripcion','habitacion')

class HabitacionesAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['habitacion']}),        
    ]
    inlines = [DispositivoInline]

class ListaComandosAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['nombre']}),        
    ]
    ordering = ['nombre']
    

admin.site.register(Habitacion,HabitacionesAdmin)
admin.site.register(ListaComandos,ListaComandosAdmin)
admin.site.register(Dispositivo,DispositivoAdmin)

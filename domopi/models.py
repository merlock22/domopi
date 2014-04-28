from django.db import models

# Create your models here.
class Habitacion(models.Model):
	habitacion = models.CharField(max_length=100)
	def __unicode__(self):
		return self.habitacion
		

class Dispositivo(models.Model):
    T_DISP=((1,'actuador'),(2,'sensor'))
    T_ACCESO=((1,"X10 PL"),(2,"X10 RF"),(3,"Arduino"))

    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=250)
    tipo_disp = models.IntegerField(choices=T_DISP,default=1)
    direccion = models.CharField(max_length=3,default=1)
    tipo_acceso = models.IntegerField(choices=T_ACCESO)
    habitacion = models.ForeignKey(Habitacion)
    def __unicode__(self):
		return self.nombre

class ListaComandos(models.Model):
	nombre = models.CharField(max_length=100)
	comando = models.CharField(max_length=10)
	def __unicode__(self):
		return self.nombre
    
class Comandos(models.Model):
	id = models.AutoField(primary_key=True)
	dispositivo = models.ForeignKey(Dispositivo)
	cmd = models.ForeignKey(ListaComandos)

class Macro(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=250)
    disp_disparador = models.ForeignKey(Dispositivo)
    cmd_disparador = models.ForeignKey(Comandos)
    def __unicode__(self):
		return self.nombre

class MacroComando(models.Model):
	macro = models.ForeignKey(Macro)	
	comando = models.ForeignKey(Comandos)
	retardo = models.IntegerField()
	n_orden = models.IntegerField()

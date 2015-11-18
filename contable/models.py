from django.db import models

class Puesto(models.Model):
    nom_puesto = models.CharField(max_length=30)
    salBase = models.FloatField()
    
class Empleado(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    salAgregado = models.FloatField()
    horas = models.IntegerField()
    horasExtras = models.IntegerField()
    dui = models.CharField(max_length=10)
    nit = models.CharField(max_length=17)
    puesto = models.ForeignKey(Puesto)
    
class TipoCuenta(models.Model):
    nom_Tipocuenta = models.CharField(max_length=30)
    
class TipoMonto (models.Model):
    nom_tipoMonto = models.CharField(max_length=30)
    
class Cuenta(models.Model):
    nom_cuenta = models.CharField(max_length=30)
    saldo = models.FloatField()
    tipoCuenta = models.ForeignKey(TipoCuenta)
    
class Transaccion(models.Model):    
    monto =  models.FloatField()
    fecha = models.DateField()
    cuenta = models.ForeignKey(Cuenta)
    tipoMonto =  models.ForeignKey(TipoMonto)
        
class EstadosCuentas(models.Model):
    periodo = models.DateField()
    cierre = models.BooleanField(default='False')
    cuenta = models.ForeignKey(Cuenta)
    tipoMonto = models.ForeignKey(TipoMonto)
    
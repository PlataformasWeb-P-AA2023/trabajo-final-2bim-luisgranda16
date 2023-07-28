from django.db import models

class Barrio(models.Model):
    nombre = models.CharField(max_length=30)
    siglas = models.CharField(max_length=30)

class Persona(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    cedula = models.CharField(max_length=30)
    correo = models.CharField(max_length=30)

class LocalComida(models.Model):
    propietario = models.ForeignKey(Persona, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=50)
    barrio = models.ForeignKey(Barrio, on_delete=models.CASCADE)  # Cambio de Persona a Barrio
    comida = models.CharField(max_length=30)
    ventas = models.FloatField()
    permiso = models.IntegerField()

    def obtenerVentas(self):
        var = self.ventas
        valorTotal = var * 0.8
        return valorTotal

class LocalRepuesto(models.Model):
    propietario = models.ForeignKey(Persona, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=50)
    barrio = models.ForeignKey(Barrio, on_delete=models.CASCADE)  # Cambio de Persona a Barrio
    valor = models.IntegerField()
    comida = models.CharField(max_length=30)
    ventas = models.IntegerField()
    permiso = models.IntegerField()

    def obtenerVentas(self):
        var = self.ventas
        valorTotal = var * 0.8
        return valorTotal
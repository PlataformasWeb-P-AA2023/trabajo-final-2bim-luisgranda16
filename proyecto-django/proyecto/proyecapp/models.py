from django.db import models

class Barrio(models.Model):
    nombre = models.CharField(max_length=30)
    siglas = models.CharField(max_length=30)
    
    def __str__(self):
        return "%s" % (self.nombre)

class Persona(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    cedula = models.CharField(max_length=30)
    correo = models.CharField(max_length=30)

    def __str__(self):
        return "%s %s" % (self.nombre, self.apellido)

class LocalComida(models.Model):
    propietario = models.ForeignKey(Persona, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=50)
    barrio = models.ForeignKey(Barrio, on_delete=models.CASCADE)  # Cambio de Persona a Barrio
    comida = models.CharField(max_length=30)
    ventas = models.FloatField()
    permiso = models.FloatField(null=True, blank=True)

    def save(self):
        self.permiso =self.ventas * 0.8
        return super(LocalComida, self).save()

    def __str__(self):
        return "%s %s %s" % (self.propietario, self.direccion, self.barrio)

class LocalRepuesto(models.Model):
    propietario = models.ForeignKey(Persona, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=50)
    barrio = models.ForeignKey(Barrio, on_delete=models.CASCADE)  # Cambio de Persona a Barrio
    valor = models.IntegerField()
    comida = models.CharField(max_length=30)
    ventas = models.IntegerField()
    permiso = models.FloatField(null=True, blank=True)

    def save(self):
        self.permiso =self.ventas * 0.001
        return super(LocalRepuesto, self).save()
    
    def __str__(self):
        return "%s %s %s" % (self.propietario, self.direccion, self.barrio)
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Curso(models.Model):

    Nombre = models.CharField(max_length=40)
    Comision = models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.Nombre}    Comision: {self.Comision}"
    

class Alumno(models.Model):

    Nombre = models.CharField(max_length=40)
    Apellido = models.CharField(max_length=40)
    Documento = models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.Nombre} Apellido: {self.Apellido} Documento: {self.Documento}"
    
class Profesor(models.Model):

    Nombre = models.CharField(max_length=40)
    Apellido = models.CharField(max_length=40)
    Documento = models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.Nombre} Apellido: {self.Apellido} Documento: {self.Documento}"
    

class Avatar(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares" , null=True , blank=True)

    def __str__(self):
        return f"User: {self.user}  -  Imagen: {self.imagen}"
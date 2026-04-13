from django.db import models

class Registro(models.Model):
    # Campos según la estructura del manual [cite: 1735-1738]
    rut = models.CharField(max_length=12)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha = models.DateField()
    descripcion = models.CharField(max_length=100)
    mensaje = models.TextField()

    class Meta:
        # Forzamos el nombre de la tabla para que coincida con el manual [cite: 1732]
        db_table = 'appReclamos_registro'

    def __str__(self):
        return f"{self.rut} - {self.nombre}"
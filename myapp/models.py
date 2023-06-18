from django.db import models

class Socio_act(models.Model):
    #id=models.AutoField(primary_key=True)
    id=models.CharField( primary_key=True, max_length=200,null=False)
    nombre=models.CharField(max_length=200, blank=False, null=False)
    apellido=models.CharField(max_length=200, blank=False, null=False)
    cedulaRUC=models.CharField(max_length=200, blank=False, null=False)
    ciudad=models.CharField(max_length=200, blank=False, null=False)
    provincia=models.CharField(max_length=200, blank=False, null=False)

    class Meta:
        verbose_name = 'Socio_act'
        verbose_name_plural = 'Socios_act'
        ordering = ['id']
    def __str__(self):
        return self.nombre 


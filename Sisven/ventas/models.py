from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre :', unique= True, blank= False, help_text= 'ingresa solo texto')
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre :', blank= False)
    precio = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='Precio :', blank= False)
    stock = models.IntegerField()
    Categoria = models.ForeignKey(Categoria, on_delete= models.RESTRICT)
    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    cedula = models.CharField(max_length=10, verbose_name= 'Cedula : ',unique= True, blank= False, null=False)
    nombre = models.CharField(max_length=50, verbose_name='Nombre del Cliente :', blank= False)
    apellido = models.CharField(max_length=50, verbose_name='Apellido del Cliente :', blank= False)
    edad = models.IntegerField()
    correo = models.EmailField()
    domicilio = models.TextField(max_length=200, help_text= 'escribe la referencia de tu domicilio')
    def __str__(self):
        return f'{self.nombre} {self.apellido}'
    
class Orden(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=4, decimal_places=2)
    Cliente = models.ForeignKey (Cliente, on_delete=models.RESTRICT)    
    Producto = models.ManyToManyField (Producto)
    def __str__(self):
        return f'Orden de {self.id} - Cliente: {self.Cliente.nombre}'
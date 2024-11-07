from django.contrib import admin

# Register your models here.
from .models import Categoria, Cliente, Orden, Producto 

admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Orden)
admin.site.register(Cliente)
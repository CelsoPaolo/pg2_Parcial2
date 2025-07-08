from django.contrib import admin
from apiconos.models import PedidoCono
from apiconos.forms import PedidoConoAdminForm # Importa el formulario personalizado

# Register your models here.

@admin.register(PedidoCono) # Decorador para registrar el modelo
class PedidoConoAdmin(admin.ModelAdmin):
    """
    Configuración del modelo PedidoCono para el panel de administración de Django.
    Utiliza un formulario personalizado para la validación de ingredientes.
    """
    form = PedidoConoAdminForm # Asigna el formulario personalizado al Admin

    # Opcional: Personaliza cómo se muestran los campos en la lista del admin
    list_display = ('cliente', 'variante', 'tamanio_cono', 'fecha_pedido', 'ingredientes_display')
    list_filter = ('variante', 'tamanio_cono', 'fecha_pedido')
    search_fields = ('cliente', 'ingredientes') # Cambiado de toppings

    def ingredientes_display(self, obj):
        """
        Método para mostrar los ingredientes de forma legible en la lista del admin.
        """
        if obj.ingredientes: # ¡ESTA ES LA LÍNEA CLAVE QUE DEBES REVISAR! Debe ser obj.ingredientes
            return ", ".join(obj.ingredientes)
        return "Ninguno"
    ingredientes_display.short_description = "Ingredientes" # Cambiado de "Toppings"
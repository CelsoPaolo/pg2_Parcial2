from django.db import models

# Create your models here.

class PedidoCono(models.Model):
    """
    Modelo para representar un pedido de cono personalizado.
    """
    cliente = models.CharField(max_length=100, help_text="Nombre del cliente que realiza el pedido.")
    
    variante = models.CharField(
        max_length=20,
        choices=[
            ("Carnívoro", "Carnívoro"),
            ("Vegetariano", "Vegetariano"),
            ("Saludable", "Saludable"),
        ],
        help_text="Tipo de variante del cono (Carnívoro, Vegetariano o Saludable)."
    )
    
    # JSONField para almacenar una lista de ingredientes adicionales.
    # Por ejemplo: ['queso_extra', 'papas_al_hilo', 'salchicha_extra']
    ingredientes = models.JSONField(default=list, help_text="Lista de ingredientes adicionales para el cono.")
    
    tamanio_cono = models.CharField(
        max_length=10,
        choices=[
            ("Pequeño", "Pequeño"),
            ("Mediano", "Mediano"),
            ("Grande", "Grande"),
        ],
        help_text="Tamaño del cono (Pequeño, Mediano o Grande)."
    )
    
    fecha_pedido = models.DateField(auto_now_add=True, help_text="Fecha en que se realizó el pedido.")

    def __str__(self):
        """
        Representación en cadena del objeto PedidoCono.
        """
        return f"Pedido de {self.cliente} - {self.variante} ({self.tamanio_cono})"

    class Meta:
        verbose_name = "Pedido de Cono"
        verbose_name_plural = "Pedidos de Conos"
        ordering = ['-fecha_pedido'] # Ordenar por fecha de pedido descendente
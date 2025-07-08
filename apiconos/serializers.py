from rest_framework import serializers
from apiconos.models import PedidoCono
from apiconos.factory import ConoFactory
from apiconos.builder import ConoPersonalizadoBuilder, ConoDirector
from apipatrones.logger import LoggerConos

class PedidoConoSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo PedidoCono.
    Define la validación para los ingredientes y atributos calculados.
    """
    precio_final = serializers.SerializerMethodField()
    ingredientes_finales = serializers.SerializerMethodField()

    class Meta:
        model = PedidoCono
        fields = '__all__' # Incluye todos los campos del modelo

    # Lista de ingredientes permitidos.
    # Esta lista es la "predefinida" que se menciona en los requisitos.
    INGREDIENTES_PERMITIDOS = [ # Cambiado de TOPPINGS_PERMITIDOS
        'queso_extra',
        'papas_al_hilo',
        'salchicha_extra',
        'jalapeños',
        'cebolla_caramelizada',
        'salsa_picante',
        'guacamole',
        'crema_agria',
        'champiñones',
        'maíz',
        'tomate_cherry',
        'aceitunas_negras',
        'piña',
        'chile_en_polvo',
        'cilantro',
    ]

    def validate_ingredientes(self, value): # Cambiado de validate_toppings
        """
        Valida que todos los ingredientes enviados estén en la lista de ingredientes permitidos.
        """
        if not isinstance(value, list):
            raise serializers.ValidationError("Los ingredientes deben ser una lista.")
        
        for ingrediente in value: # Cambiado de topping
            if not isinstance(ingrediente, str):
                raise serializers.ValidationError("Cada ingrediente en la lista debe ser un texto.")
            if ingrediente not in self.INGREDIENTES_PERMITIDOS: # Cambiado de TOPPINGS_PERMITIDOS
                # Mensaje de error actualizado
                raise serializers.ValidationError(f"El ingrediente '{ingrediente}' no está disponible.") 
        return value

    def _build_cono_and_get_builder(self, obj):
        """
        Método auxiliar para centralizar la lógica de construcción del cono.
        """
        # Patrón Factory: Obtener la base del cono según la variante
        cono_base = ConoFactory.obtener_cono_base(obj.variante)
        
        # Patrón Builder: Inicializar el constructor con la base del cono
        builder = ConoPersonalizadoBuilder(cono_base)
        director = ConoDirector(builder)
        
        # ¡ESTA ES LA LÍNEA CLAVE QUE DEBES REVISAR!
        # Asegúrate de que aquí diga obj.ingredientes y no obj.toppings
        ingredientes_a_procesar = obj.ingredientes if isinstance(obj.ingredientes, list) else [] # <-- ¡Aquí está el cambio!
        
        director.construir(ingredientes_a_procesar, obj.tamanio_cono)
        
        return builder

    def get_precio_final(self, obj):
        """Calcula el precio final del pedido de cono."""
        builder = self._build_cono_and_get_builder(obj)
        LoggerConos().registrar(f"Se calculó el precio final para el pedido de cono {obj.id}")
        return builder.obtener_precio_final()

    def get_ingredientes_finales(self, obj):
        """Obtiene la lista completa de ingredientes del cono."""
        builder = self._build_cono_and_get_builder(obj)
        LoggerConos().registrar(
            f"Se obtuvieron los ingredientes finales para el pedido de cono {obj.id}"
        )
        return builder.obtener_ingredientes_finales()
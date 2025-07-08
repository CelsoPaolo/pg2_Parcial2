class ConoPersonalizadoBuilder:
    """
    Constructor (Builder) para ensamblar un cono personalizado paso a paso.
    """
    def __init__(self, cono_base):
        """
        Inicializa el constructor con un cono base (creado por el Factory).
        """
        self.base = cono_base
        self.precio = cono_base.obtener_precio_base()
        self.ingredientes = list(cono_base.obtener_ingredientes_base())

    def agregar_ingrediente(self, ingrediente):
        """
        Añade un ingrediente al cono y ajusta el precio.
        Los precios de los ingredientes se definen aquí.
        """
        precios_ingredientes = {
            "queso_extra": 3.0,
            "queso": 1.5, # Añadido 'queso' con un precio para que sea reconocido
            "papas_al_hilo": 2.5,
            "salchicha_extra": 4.0,
            "jalapeños": 1.5,
            "cebolla_caramelizada": 2.0,
            "salsa_picante": 1.0,
            "guacamole": 3.5,
            "crema_agria": 2.0,
            "champiñones": 2.5,
            "maíz": 1.0,
            "tomate_cherry": 1.5,
            "aceitunas_negras": 2.0,
            "piña": 1.5,
            "chile_en_polvo": 0.5,
            "cilantro": 0.5,
            "carne": 4.2,
            "pollo": 2.0,
            "lechuga": 0.5,
        }
        
        # Se asume que el ingrediente ya ha sido validado por el serializador.
        if ingrediente not in precios_ingredientes:
            raise ValueError(f"Ingrediente '{ingrediente}' no válido o no disponible en el Builder.")

        self.ingredientes.append(ingrediente)
        self.precio += precios_ingredientes.get(ingrediente, 0)

    def ajustar_tamanio(self, tamanio):
        """
        Ajusta el precio del cono según su tamaño.
        """
        if tamanio == "Mediano":
            self.precio *= 1.2
        elif tamanio == "Grande":
            self.precio *= 1.4

    def obtener_precio_final(self):
        """Devuelve el precio final calculado del cono."""
        return round(self.precio, 2)

    def obtener_ingredientes_finales(self):
        """Devuelve la lista completa de ingredientes del cono."""
        return self.ingredientes


class ConoDirector:
    """
    Director para el Patrón Builder. Orquesta los pasos de construcción del cono.
    """
    def __init__(self, builder):
        """
        Inicializa el Director con una instancia del ConoPersonalizadoBuilder.
        """
        self.builder = builder

    def construir(self, ingredientes, tamanio):
        """
        Construye un cono personalizado añadiendo los ingredientes y ajustando el tamaño.
        """
        for ingrediente in ingredientes:
            self.builder.agregar_ingrediente(ingrediente)
        self.builder.ajustar_tamanio(tamanio)
    
    # Opcional: Métodos para construir conos predefinidos (combos)
    def construir_combo_picante(self):
        """Construye un cono con un set predefinido de ingredientes picantes."""
        self.builder.agregar_ingrediente("jalapeños")
        self.builder.agregar_ingrediente("salsa_picante")
        self.builder.ajustar_tamanio("Mediano")

    def construir_combo_veggie(self):
        """Construye un cono con un set predefinido de ingredientes vegetarianos."""
        self.builder.agregar_ingrediente("champiñones")
        self.builder.agregar_ingrediente("maíz")
        self.builder.ajustar_tamanio("Pequeño")
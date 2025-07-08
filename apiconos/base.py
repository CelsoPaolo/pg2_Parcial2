import abc

class ConoBase(abc.ABC):
    """
    Clase base abstracta para los diferentes tipos de conos (Carnívoro, Vegetariano, Saludable).
    Define la interfaz común para los conos.
    """
    def __init__(self):
        self.ingredientes_base = []
        self.precio_base = 0.0

    @abc.abstractmethod
    def inicializar(self):
        """
        Método abstracto para definir los ingredientes y el precio base de cada variante de cono.
        Debe ser implementado por las subclases concretas.
        """
        pass

    def obtener_ingredientes_base(self):
        """Devuelve la lista de ingredientes base del cono."""
        return self.ingredientes_base

    def obtener_precio_base(self):
        """Devuelve el precio base del cono."""
        return self.precio_base


class ConoCarnivoro(ConoBase):
    """Implementación concreta de un cono Carnívoro."""
    def inicializar(self):
        self.ingredientes_base = ["carne_asada", "papas_fritas", "salsa_barbacoa"]
        self.precio_base = 25.0


class ConoVegetariano(ConoBase):
    """Implementación concreta de un cono Vegetariano."""
    def inicializar(self):
        self.ingredientes_base = ["falafel", "hummus", "pepinillos", "salsa_yogur"]
        self.precio_base = 22.0


class ConoSaludable(ConoBase):
    """Implementación concreta de un cono Saludable."""
    def inicializar(self):
        self.ingredientes_base = ["pollo_a_la_plancha", "quinoa", "vegetales_frescos", "aderezo_ligero"]
        self.precio_base = 28.0
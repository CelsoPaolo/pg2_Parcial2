from apiconos.base import ConoCarnivoro, ConoVegetariano, ConoSaludable

class ConoFactory:
    """
    Patrón Factory para crear instancias de ConoBase según la variante solicitada.
    """
    @staticmethod
    def obtener_cono_base(variante):
        """
        Crea y devuelve una instancia de ConoBase (Carnívoro, Vegetariano o Saludable)
        basándose en la variante especificada.
        """
        if variante == "Carnívoro":
            cono = ConoCarnivoro()
        elif variante == "Vegetariano":
            cono = ConoVegetariano()
        elif variante == "Saludable":
            cono = ConoSaludable()
        else:
            raise ValueError(f"Variante de cono '{variante}' no válida.")
        
        cono.inicializar() # Asegura que los ingredientes y precio base estén configurados
        return cono
class LoggerConos:
    """
    Patrón Singleton para una clase de registro (logger) específica para la API de conos.
    Asegura que solo exista una instancia de esta clase en toda la aplicación.
    """
    _instancia = None
    _initialized = False # Bandera para asegurar que la inicialización se haga una sola vez

    def __new__(cls):
        """
        Controla la creación de instancias para asegurar que solo haya una.
        """
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
        return cls._instancia

    def __init__(self):
        """
        Inicializa la instancia del logger (solo se ejecuta una vez).
        """
        if not self._initialized:
            self.logs = []
            self._initialized = True

    def registrar(self, mensaje):
        """
        Registra un mensaje en la lista de logs.
        """
        self.logs.append(mensaje)

    def obtener_logs(self):
        """
        Devuelve todos los mensajes registrados.
        """
        return self.logs
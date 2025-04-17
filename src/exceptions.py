class NumeroDebeSerPositivo(Exception):
    """Excepción que se lanza cuando un número no es positivo."""
    
    def __init__(self, mensaje="El número debe ser positivo (mayor que cero)."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)
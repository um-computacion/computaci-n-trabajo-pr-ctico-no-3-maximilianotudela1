class NumeroDebeSerPositivo(Exception):
    
    def __init__(self, mensaje="El número debe ser positivo (mayor que cero)."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)
        
        from src.exceptions import NumeroDebeSerPositivo

def ingrese_numero():
    
    try:
        numero = float(input("Ingrese un número: "))
        
        if numero <= 0:
            raise NumeroDebeSerPositivo()
            
        return numero
    except ValueError:
        raise ValueError("La entrada debe ser un número válido.")
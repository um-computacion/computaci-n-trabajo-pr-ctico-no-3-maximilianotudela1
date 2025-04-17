from src.exceptions import NumeroDebeSerPositivo

def ingrese_numero():
    """
    Solicita al usuario ingresar un número y valida que sea positivo.
    
    Returns:
        float: El número ingresado si es válido y positivo.
        
    Raises:
        ValueError: Si la entrada no es un número válido.
        NumeroDebeSerPositivo: Si el número es negativo o cero.
    """
    try:
        numero = float(input("Ingrese un número: "))
        
        if numero <= 0:
            raise NumeroDebeSerPositivo()
            
        return numero
    except ValueError:
        raise ValueError("La entrada debe ser un número válido.")
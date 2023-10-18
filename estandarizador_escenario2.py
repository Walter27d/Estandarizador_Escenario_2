import re
import patrones_escenario2

def limpiar_cadena(cadena):
    cadena_limpia = re.sub(r'[^a-zA-Z0-9\s]', '', cadena)
    return cadena_limpia

def estandarizar_direccion(cadena):
    direccion = limpiar_cadena(cadena)
    direccion = direccion.upper()
    return patrones_escenario2.extraer_componentes_direccion_escenario2(direccion)

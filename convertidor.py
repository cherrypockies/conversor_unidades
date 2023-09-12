import temperatura
import masa
import tiempo

def convertir_temperatura(valor, unidad_origen, unidad_destino):
    if unidad_origen == "celsius" and unidad_destino == "farenheit":
        return temperatura.celsius_farenheit(valor)
    
def convertir_masa(valor, unidad_origen, unidad_destino):
    if unidad_origen == "kilogramos" and unidad_destino == "gramos":
        return masa.kg_g(valor)
    
def convertir_tiempo(valor, unidad_origen, unidad_destino):
    if unidad_origen == "segundos" and unidad_destino == "minutos":
        return tiempo.seg_min(valor)

if __name__ == "__main__":
    valor = 20
    unidad_origen = "celsius"
    unidad_destino = "farenheit"
    resultado = convertir_temperatura(valor, unidad_origen, unidad_destino)
    print(f"{valor} grados {unidad_origen} equivalen a {resultado} grados {unidad_destino}")
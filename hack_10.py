"""
text: [{"a":"b"},{"c","d"},{"e":"f"}] output => [{"1":"2"},{"3","4"},{"5":"6"}]
"""


def fn_hack_10(lista_entrada):
    # Inicializar el contador
    contador = 1
    # Inicializar la lista de salida
    lista_salida = []
    
    # Procesar cada diccionario en la lista de entrada
    for diccionario in lista_entrada:
        nuevo_diccionario = {}
        # Procesar cada par clave-valor en el diccionario
        for clave, valor in diccionario.items():
            # Reemplazar la clave y el valor con el contador convertido a cadena
            nueva_clave = str(contador)
            contador += 1
            nuevo_valor = str(contador)
            contador += 1
            # Agregar el nuevo par clave-valor al nuevo diccionario
            nuevo_diccionario[nueva_clave] = nuevo_valor
        # Agregar el nuevo diccionario a la lista de salida
        lista_salida.append(nuevo_diccionario)
    

    result = lista_salida
    return result


#print(fn_hack_10([{"a":"b"},{"c","d"},{"e":"f"}]))

#entrada = [{"a":"b"},{"c":"d"},{"e":"f"}]
#salida = fn_hack_10(entrada)
#print(salida)  # Debería imprimir: [{"1":"2"},{"3":"4"},{"5":"6"}]

# Ejemplo de uso
print(fn_hack_10([{"a":"b"},{"c":"d"},{"e":"f"}]))

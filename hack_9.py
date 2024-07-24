"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""


def fn_hack_9(s):
    result = s
    salida = {}
    
    # Procesar cada par clave-valor en el diccionario de entrada
    for clave, valor in result.items():
        if clave.lower() == "foo":
            # Transformar la clave y el valor según lo especificado
            nueva_clave = "Foo"
            nuevo_valor = valor.replace("k", "").capitalize()
            # Agregar el nuevo par clave-valor al diccionario de salida
            salida[nueva_clave] = nuevo_valor
    
    result = salida
    return result

# Ejemplo de uso
s = {"foo":"fookziman","Fooo":"barkziman"}
salida = fn_hack_9(s)
print(salida)  # Debería imprimir: {"Foo":"Fooziman"}



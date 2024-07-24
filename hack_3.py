"""
generic script

a = @

i = ¡
o = 0
u = v

text: "fooziman" output => "F00z¡m@N" 
text: "barziman" output => "B@rz¡m@N" 
text: "3q" output => "3Q" 
text: "qu" output => "Qv" 
text: "qux" output => "QvX" 
"""


def fn_hack_3(s):
    tabla_traduccion = str.maketrans({
        'a': '@',
        'e': '3',
        'i': '¡',
        'o': '0',
        'u': 'v'
                
    })
    #traducir el texto
    texto_traducido = s.translate(tabla_traduccion)
    #hacer mayuscula la primera y ultima letra
    resultado = texto_traducido[0].upper() + texto_traducido[1:-1] + texto_traducido[-1].upper()
    #validar que la palabra termina en V y cambiarla por v
    if resultado[-1] == 'V':
        resultado= resultado[:-1] + 'v'

    return resultado

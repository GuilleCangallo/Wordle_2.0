def encontrar_letra_palabra(palabra, letra):
    enumarador_palabra = enumerate(palabra)
    return [pos for pos, c in enumarador_palabra if c == letra]

def comparar_palabras(palabra1, palabra2):
    return []

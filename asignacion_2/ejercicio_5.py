"""
    
5. Validador de Laboratorio: El programa debe preguntar el número de laboratorio. Si
el usuario ingresa "LF6-LAB", permite el acceso; de lo contrario, indica "Aula
incorrecta".

"""
# guardamos el código correcto en una constante
AULA_CORRECTA = "LF6-LAB"

# Solicitamos el dato limpiando los espacioos al inicio y al final
aula_ingresada = input("Ingrese el número del laboratorio: ").strip()

# validmaos ignorando si el usuario escribe en mayúsculas o minúsculas
if aula_ingresada.upper() == AULA_CORRECTA:
    print("Acceso Permitido")
else:
    print("Aula incorrecta")
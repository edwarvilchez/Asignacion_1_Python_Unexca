"""
6. Descuento en Inscripción: Si un estudiante tiene un promedio superior a 18, aplica
un 15% de descuento a su matrícula. Muestra el monto final a pagar.

"""

PROMEDIO_MINIMO_DESCUENTO = 18.
PORCENTAJE_DESCUENTO = 0.15 # 15 / 100

# capturamos el dato de forma limpia

matricula_base = float(input("Ingrese el monto de la Matrícula: "))
promedio = float(input("Ingrese el promedio del estudiante (0-20): "))

# validamos que el promedio sea mayor a 18
if 0 <= promedio <= 20:
    if promedio > PROMEDIO_MINIMO_DESCUENTO:
        descuento = matricula_base * PORCENTAJE_DESCUENTO
        monto_final = matricula_base - descuento
        print(f"Felicidades!. Aplica descuento del 15%. El monto final a pagar es {monto_final: .2f}")
    else:
        print(f"No aplica el descuento. El monto final a pagar es: {matricula_base: .2f}")
else:
    print("Error: El promedio debe estar entre 0 y 20")

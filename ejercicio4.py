"""
Escribir una función que calcule el total de una factura tras aplicarle el IVA.
+ La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, 
y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje 
de IVA, deberá aplicar un 21%.
"""
def total_factura(cantidad, porcentaje=21):
   return cantidad + (cantidad*porcentaje)/100
cantidad = 0
cantidad = float(input("Ingrese la cantidad sin IVA del producto a comprar: "))
iva = 0
iva = int(input("Ingrese el valor del IVA: "))
print(f"El total de la factura es: {total_factura(cantidad,iva)}") 

####Realizar una función anidada que genere la potencia de un número entero
def generador_potencia(exponente):

    def potencia(base):
        return base**exponente

    return potencia

#### Desarrollamos la parte externa de la aplicación
elevar_cuadrado = generador_potencia(2)
print(f" El cuadrado es: {elevar_cuadrado(5)}")

elevar_cubo = generador_potencia(3)
print(f"El cubo es: {elevar_cubo(4)}")


####Realizar una función anidada que genere la potencia de un número entero
def generador_potencia(exponente):

    def potencia(base):
        return base**exponente

    return potencia

#### Desarrollamos la parte externa de la aplicación
elevar_cuadrado = generador_potencia(2)
print(" El cuadrado es: ",elevar_cuadrado(5))##Cambios realizados en la sálida de datos

elevar_cubo = generador_potencia(3)##Calculo de la potencia al cubo
print(f"El cubo es: {elevar_cubo(4)}")


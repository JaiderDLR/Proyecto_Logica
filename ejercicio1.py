def operaciones_basicas(n1, n2):#Función Externa

    def suma():#función interna 1
        return n1+n2

    def mult():#Función interna 2
        return n1*n2
    
    return suma(), mult()

#### Fuera de la función operaciones básicas

print(f"El resultado de la suma y la multiplación es = {operaciones_basicas(4,5)}")

##comentario de pull request




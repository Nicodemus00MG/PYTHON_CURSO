'''
Escribir un programa que lea un entero positivo, n, 
introducido por el usuario y después muestre en
 pantalla la suma de todos los enteros desde 1 hasta n La suma de los
 primeros enteros positivos puede ser calculada de la siguiente forma:


 sumatoria= n(n+1)/2

'''

numero=int(input("Ingrese numero entero: "))

funcion= 0
sumatoria=0
contador=1
while(contador<=numero):
    funcion = (contador*(contador+1))/(2);
    print("cuando i=",contador,"la sumatoria es: ",funcion)
    sumatoria=sumatoria+funcion

    contador=contador+1

#i=1
#f(1)= (1*(1+1))/2
    

    print("resultado de sumatoria: ", sumatoria)

    
#esto es un comentario de una sola linea
#esto es un segundo comentariod de solo una linea


#dasdadasdsd

'''

'''
'''

esto es un bloque de comentario o comentario de multiples lineas


asdasda

dsadasd

'''


#numericas, String, char, booleanes


#para definir en python variables , 


# int numero1= 5;
# <nombre de la variable> = <valor de dicha variable> ;


#variables booleanas = True o False (validaciones)
#numero1 = 10 ;

#numero2 = 15;

#numero3=numero1+numero2;
#print(numero3)

#print('HOLAMUNDO')

# CREAR UNA CALCULADORA , SUMAR , RESTAR, MULTIPLICAR Y DIVIDIR  2 NUMEROS, E IMPRIMIR EL RESULTADO

#1. pedir datos, numeros (2)
#2. imprimir el resultado de la suma , resta, multiplcacion y division segun este ejemplo :  num1=3 y num2=5    '
#suma: 8    
#resta: -2 , 
#producto: 15 
#division : 0.6


#  pedir datos al usuario: -->input() 
# ! solamente va a recibir datos de tipo str
# casteo , conversion de tipo de datos    int(input())-> "5" -> 5
'''




print("Ingrese numero1: ")
numero1= int(input()) 

print("Ingrese numero2:")
numero2= int(input())


print("SUMA: ",numero1+numero2)
print("RESTA: ",numero1-numero2)
print("PRODUCTO: ", numero1*numero2)
print("DIVISION: ", numero1/numero2)


'''




#print("numero ya guardado", numero1)
#print(type(numero1)) #--> imprimir el tipo de dato de la variable 

# cadenas de caracteres (str-strings)

#crear un programa que me imprima los dias de la semana , con el siguiente saludo: "buenos dias A, hoy es B", A EL NOMBRE DEL USUARIO Y B EL DIA DE LA SEMANA , 

#IMPRIMIR 7 VECES EL SALUDO CON TODOS LOS DIAS DE LA SEMANA 

#1. CREAR O PLANTEAR DATOS O VARIABLES

#2. PEDIR : NOMBRE_USUARIO, 

#3. IMPRIMO SALUDO CON NOMBRE CON LOS 7 DIAS DE LA SEMAANA 
'''

print("INGRESE NOMBRE DE USUARIO: ")
nombreUsuario=input()

print("HOLA ",nombreUsuario,"HOY ES LUNES.")
print("HOLA ",nombreUsuario,"HOY ES MARTES.")

print("HOLA ",nombreUsuario,"HOY ES MIERCOLES.")
print("HOLA ",nombreUsuario,"HOY ES JUEVES.")
print("HOLA ",nombreUsuario,"HOY ES SABADO.")
print("HOLA ",nombreUsuario,"HOY ES DOMINGO.")
'''
'''
Ejercicio 2

Escribir un programa que almacene la cadena 
¡Hola Mundo! en una variable y luego muestre
 por pantalla el contenido de la variable.

'''
# saludo="¡HOLA MUNDO!"
# print(saludo)



# print("holamundo")



'''
Escribir un programa que pregunte el nombre del usuario en la consola y después de 
que el usuario lo introduzca muestre por pantalla la cadena ¡Hola <nombre>!,
 donde <nombre> es el nombre que el usuario haya introducido.

'''


# nombre=input("INGRESE NOMBRE: ")
# print("hola! ",nombre)



#1. RESULTADO

# resultado= ((3+2)/(2*5))**2
# print(resultado)





'''
Escribir un programa que pregunte al usuario por el 
número de horas trabajadas y el coste por hora.

!   print(coste*numero_horas)
 Después debe mostrar por pantalla la paga que le corresponde.

'''

costeHora=int(input("Ingrese el coste por hora de trabajo: "))
numeroHorasTrabajadas=int(input("Ingrese numero horas trabajadas: "))

print("TOTAL PAGA POR NUMERO HORAS TRABAJAS: ",costeHora*numeroHorasTrabajadas)








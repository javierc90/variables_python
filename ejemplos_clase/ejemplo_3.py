# Tipos de variables [Python]
# Ejemplos de clase

# Autor: Inove Coding School
# Version: 2.0

# Ejemplos capturando información desde la consola

# Comencemos a ingresar datos por medio de la consola
# Primero mostraremos en pantalla el dato deseado a ingresar
# y luego esperaremos por el
print('Ingrese su nombre:')
nombre = str(input())
print('Nombre ingresado:', nombre)

print('Ingrese cuantos años tiene:')
edad = str(input())
edad = int(edad)
print('Edad ingresada:', edad)

numero_1 = input("Ingrese un número: ")
numero_2 = input("Ingrese un número: ")

resultado = numero_1+numero_2
print(resultado)
numero_1 = int(numero_1)
numero_2 = int(numero_2)
resultado = numero_1+numero_2
print(resultado)

print('Ingrese su altura en metros:')
altura = float(input())
print('Altura ingresada:', altura)

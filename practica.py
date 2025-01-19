#primer ejercicio
print("Hola mundo :p")

#segundo ejercicio
saludo = input("Ingrese su nombre: ")
print("Hola,", saludo)

#tercer ejercicio
edad  = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Mayor de edad")
else:
    print("Menor de edad")

#cuarto ejercicio
numero = int(input("Ingrese un número entero: "))
if numero % 2 == 0:
    print(numero, "es par")
else:
    print(numero, "es impar")

#quinto ejercico
numero = int(input("Ingrese un número entero: "))
suma = numero * (numero + 1) // 2
print(f"La suma de los numeros desde 1 hasta {numero} es: {suma}")
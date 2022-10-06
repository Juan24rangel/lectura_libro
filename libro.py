# Hacer el diagrama de flujo y programa en Python, que lea números enteros y positivos(uno en cada lectura), y que averigue e imprima cuantos son pares y cuantos son impares. Para terminar utilizaremos el registro centinela para cuando el valor del número leído sea 0.

#input
num = int(input("Digite el numero: "))

#processing
while (num!=0):
    x=print(" es neutro ")
    if num>0:
        if num/2:
            x = print("Es un numero positivo par.")
        else:
            x = print("Es un numero positivo impar.")
    if num<0:
        if num/2:
            x=print("Es un numero negativo par.")
        else:
            x = print("Es un numero negativo impar.")

#output

print("Registro: " +str(x))
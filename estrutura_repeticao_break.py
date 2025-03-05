while True:    
    numero = int(input("Informe um numero: "))

    if numero == 10:
        break

    print(numero)

print(" ")

for numero in range (1000):
    
    if numero == 20:
        break

    print(numero, end=" ")

print(" ")

for numero in range (100):
    
    if numero == 20:
        continue

    print(numero, end=" ")

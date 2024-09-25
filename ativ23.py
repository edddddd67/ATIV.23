# Crie um programa que receba um número do usuário e exiba a tabuada desse número de 1 a 10.
nm = int(input('digite um numero para ver sua tabuada'))
print(f"tabuada do {nm}:")
for tabuada in range(1, 11):
    resultado = nm * tabuada
    print (f"{nm} x {tabuada}")
    
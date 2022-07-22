resp = ''
par = 0
impar = 0

while resp in 'SsSIMSimsim':
    x = int(input("Digite um valor inteiro: "))

    if x % 2 == 0:
        par += 1
    else:
        impar += 1

    resp = input("Desejar continuar [S/N]: ")

print(f"PARES: {par}")
print(f"ÍMPARES: {impar}")


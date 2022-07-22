resp = ''

x = int(input("Digite um valor inteiro: "))

maior = x
menor = x
total = x

resp = input("Deseja continuar [S/N]: ")

while resp in 'SsSIMSim':
    x = int(input("Digite um valor inteiro: "))

    total += x

    if x > maior:
        maior = x

    if x < menor:
        menor = x

    resp = input("Deseja continuar [S/N]: ")

print(f"MAIOR VALOR: {maior}")
print(f"MENOR VALOR: {menor}")
print(f"SOMA TOTAL: {total}")
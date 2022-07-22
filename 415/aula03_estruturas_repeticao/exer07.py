resp = ''
total = 0
count = 0

while resp in 'SsSimSIM':
    total += int(input("Digite um valor inteiro: "))
    count += 1

    resp = input("Deseja continuar [S/N]: ")

print(f"A média será: {total / count:.2f}")

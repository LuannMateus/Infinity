resp = ''
total = 0
count = 0

while resp in 'SsSimSIM':
    total += int(input("Digite a idade: "))

    count += 1

    resp = input("Deseja continuar [S/N]: ")


media = int(total / count)

if 0 <= media <= 25:
    print("Jovem!")
elif 26 <= media <= 60:
    print("Adulta!")
elif media > 60:
    print("Idosa")
else:
    print("Média inválida")

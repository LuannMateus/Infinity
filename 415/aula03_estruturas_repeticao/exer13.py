count = 0

x = int(input("Digite um valor inteiro: "))

for i in range(1, x + 1):
    if x % i == 0:
        count += 1

if count > 2:
    print(f"{x} não é primo")
else:
    print(f"{x} é primo")


fatorial = 1

x = int(input("Digite um valor para ser fatorado: "))

for i in range(x, 0, -1):
    fatorial *= i

print(f"O fatorial de {x} é {fatorial}")
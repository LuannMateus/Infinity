n = int(input("Digite a quatidade de maças compradas: "))

if n < 12:
    preco_total = n * 1.3
else:
    preco_total = n * 1

print(f"VALOR FINAL: {preco_total}")

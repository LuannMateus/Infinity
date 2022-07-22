count_negativo = 0

for i in range(0, 10):
    x = int(input(f"Digite o {i + 1} número: "))

    if x < 0:
        count_negativo += 1

print(f"TOTAL VALORES NEGATIVOS: {count_negativo}")
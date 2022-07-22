total = 0

for i in range(0, 10):
    x = int(input(f"Digite o {i + 1} número: "))

    if x < 40:
        total += x

print(f"A soma total será {total}")
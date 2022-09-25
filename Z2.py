# Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

print('x\ty\tz\tF')
for x in range(2):
    for y in range(2):
        for z in range(2):
            F = not (x or y or z)
            print(f'{x}\t{y}\t{z}\t{bool(F)}')
print('¬x\t¬y\t¬z\t¬F')
for x in range(1,-1,-1):
    for y in range(1,-1,-1):
        for z in range(1,-1,-1):
            Fx = not x and not y and not z
            print(f'{x}\t{y}\t{z}\t{bool(Fx)}')
n = int(input("Введите количество ступенек\n"))
for i in range(1, n + 1):
    for x in range(1, i + 1):
        print(x, sep='', end='')
    print()

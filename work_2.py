numbers = int(input("Введите число N: "))
count = 0
trymp = numbers

while trymp > 0:
    trymp //= 10
    count += 1


for n in range(1, numbers):
    for rof in range(1, count + 1):
        if n == n * n % 10 ** rof:
            print(n, "*", n, "=", n * n)
            break

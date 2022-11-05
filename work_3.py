number = 0
count = 0
sum = 0
average = 0
maximum, minimum = 0, 0
even, odd = 0, 0

while True:
    number = int(input("Enter the number: "))

    if number == 0:
        break

    count += 1
    sum += number

    if count == 1:
        minimum = number
    if number > maximum:
        maximum = number
    elif number < minimum:
        minimum = number

    if number % 2 == 0:
        even += 1
    else:
        odd += 1
count +=1
average = sum / count

print("Сумма чисел -", sum)
print("Среднее арифмитическое -", average)
print("Максимальное =", maximum, "Минимальное -", minimum)
print("Количество парных -", even, "количество непарных -", odd)
print()

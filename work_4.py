guess_number = int(input("Введите число: "))

print(guess_number, end=" ")

for number in range(1, guess_number):
    squere = number ** 2
    if squere < guess_number:
        print(squere, end=" ")
    else:
        break
print()

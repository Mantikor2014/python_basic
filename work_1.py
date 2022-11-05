number_string = input("Введите номер: ")
message = "NO"

for number in number_string:
    Counter = number_string.count(number)

    if Counter > 1:
        message = "YES"
        break

print(message)

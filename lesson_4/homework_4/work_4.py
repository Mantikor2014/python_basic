year = int(input("Введите год:"))

if year < 1900:
    print("Введен неверный год")
elif year > 1000000:
    print("Введен неверний год")
else:
    if not year % 400:
        print("Високосный", year, "год")
    else:
        if year % 4:
            print("Обычный", year, "год")
        else:
            if not year % 100:
                print("Обычный", year, "год")
            else:
                print("Високосный", year, "год")

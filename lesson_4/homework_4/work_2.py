"""work_2"""
CABINETS_AMOUNT = 3
STUDENTS_PER_DESC = 2

first_class_students_amount = int(
    input("Введите количество студентов в первом классе: ")
)
second_class_students_amount = int(
    input("Введите количество студентов во втором классе: ")
)
third_class_students_amount = int(
    input("Введите количество студентов в третьем классе: ")
)

total_students_amount = (
    first_class_students_amount
    + second_class_students_amount
    + third_class_students_amount
)

desks_amount = (
    total_students_amount // STUDENTS_PER_DESC
    + total_students_amount % STUDENTS_PER_DESC
)

print("Общее количество парт для учеников: ", desks_amount)

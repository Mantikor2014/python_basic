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


desks_amount_1 = (
     first_class_students_amount // STUDENTS_PER_DESC
    + first_class_students_amount % STUDENTS_PER_DESC
)
desks_amount_2 = (
    second_class_students_amount // STUDENTS_PER_DESC
    + second_class_students_amount % STUDENTS_PER_DESC
)
desks_amount_3 = (
    third_class_students_amount // STUDENTS_PER_DESC
    + third_class_students_amount % STUDENTS_PER_DESC
)
general_desks_amount = (desks_amount_1 + desks_amount_2 + desks_amount_3
)
print("Общее количество парт для учеников: ", general_desks_amount)

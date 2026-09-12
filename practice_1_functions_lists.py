def calculate_average(grades):
    """Возвращает среднее значение списка оценок."""
    if len(grades) == 0:
        return 0
    return sum(grades) / len(grades)

def count_passed(grades):
    """Считает оценки не ниже тройки."""
    count = 0
    for grade in grades:
        if grade >= 3:
            count += 1
    return count

def get_status(average):
    """Определяет итоговый статус по среднему баллу."""
    if average >= 3:
        return "зачёт"
    return "незачёт"

def print_report(name, grades):
    """Печатает отчёт по одному студенту."""
    average = calculate_average(grades)
    passed = count_passed(grades)
    
    print("Студент:", name)
    print("Оценки:", grades)
    print(f"Средний балл: {average:.2f}")
    print("Положительных оценок:", passed)
    print("Результат:", get_status(average))

student_name = "Артем"
student_grades = []
print_report(student_name, student_grades)


def analyze_grades(grades):
    
    unique_grades = tuple(sorted(set(grades)))
    
    average_grade = sum(grades) / len(grades)
    
    good_students = len([grade for grade in grades if grade >= 7])
    
    has_excellent = 10 in grades
    
    return unique_grades, average_grade, good_students, has_excellent


test_cases = [
    [5, 7, 8, 6, 9, 7, 10, 8, 6, 7],  
    [3, 4, 5, 6, 4, 5, 3, 6, 5, 4],   
    [8, 9, 10, 9, 10, 8, 9, 10, 9, 8] 
]

for i, grades in enumerate(test_cases, 1):
    print(f"Тест {i}:")
    print(f"Оценки: {grades}")
    
    unique, average, good_count, has_excellent = analyze_grades(grades)
    
    print(f"Уникальные оценки: {unique}")
    print(f"Средний балл: {average:.2f}")
    print(f"Студентов с оценкой 7+: {good_count}")
    print(f"Есть отличники: {'Да' if has_excellent else 'Нет'}")
    print("-" * 40)
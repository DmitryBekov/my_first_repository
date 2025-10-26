def student_grades_manager():
    """
    Программа для учета оценок студентов.
    Позволяет добавлять, просматривать и вычислять средний балл.
    """
    def add_grade():
        name = input("Введите имя студента: ")
        subject = input("Введите предмет: ")
        grade = input("Введите оценку: ")
        
        with open('grades.txt', 'a', encoding='utf-8') as file:
            file.write(f"{name} | {subject} | {grade}\n")
        
        print("Оценка добавлена!")
    
    def view_grades():
        try:
            with open('grades.txt', 'r', encoding='utf-8') as file:
                grades = file.readlines()
            
            if not grades:
                print("Оценки не найдены.")
                return
            
            print("\n--- ОЦЕНКИ СТУДЕНТОВ ---")
            for grade in grades:
                print(grade.strip())
        
        except FileNotFoundError:
            print("Файл с оценками не найден.")
    
    def calculate_average():
        try:
            with open('grades.txt', 'r', encoding='utf-8') as file:
                grades = file.readlines()
            
            if not grades:
                print("Оценки не найдены.")
                return
            
            total = 0
            count = 0
            
            for grade_line in grades:
                parts = grade_line.strip().split(' | ')
                if len(parts) >= 3:
                    try:
                        total += int(parts[2])
                        count += 1
                    except ValueError:
                        continue
            
            if count > 0:
                average = total / count
                print(f"Средний балл: {average:.2f}")
            else:
                print("Нет действительных оценок.")
        
        except FileNotFoundError:
            print("Файл с оценками не найден.")
    
    while True:
        print("\n--- УЧЕТ ОЦЕНОК СТУДЕНТОВ ---")
        print("1. Добавить оценку")
        print("2. Просмотреть оценки")
        print("3. Средний балл")
        print("4. Выход")
        
        choice = input("Выберите действие: ")
        
        if choice == '1':
            add_grade()
        elif choice == '2':
            view_grades()
        elif choice == '3':
            calculate_average()
        elif choice == '4':
            break
        else:
            print("Неверный выбор")

# Запуск программы
student_grades_manager()
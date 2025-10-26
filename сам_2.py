import datetime

def add_expense():
    category = input("Введите категорию расхода: ")
    amount = float(input("Введите сумму расхода: "))
    description = input("Введите описание расхода: ")
    
    with open('expenses.txt', 'a', encoding='utf-8') as file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp} | {category} | {amount} | {description}\n")
    
    print("Расход успешно добавлен!")

def show_expenses():
    try:
        with open('expenses.txt', 'r', encoding='utf-8') as file:
            expenses = file.readlines()
        
        if not expenses:
            print("Расходы не найдены.")
            return
        
        print("\n--- ВАШИ РАСХОДЫ ---")
        total = 0
        for expense in expenses:
            print(expense.strip())
            parts = expense.split(' | ')
            total += float(parts[2])
        print(f"\nОбщая сумма расходов: {total}")
    
    except FileNotFoundError:
        print("Файл с расходами не найден.")

def main():
    while True:
        print("\n1. Добавить расход")
        print("2. Показать расходы")
        print("3. Выход")
        
        choice = input("Выберите действие: ")
        
        if choice == '1':
            add_expense()
        elif choice == '2':
            show_expenses()
        elif choice == '3':
            break
        else:
            print("Неверный выбор")

if __name__ == "__main__":
    main()
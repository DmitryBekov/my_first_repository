class EmptyFileError(Exception):
    pass

def check_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read().strip()
            if not content:
                raise EmptyFileError("файл пустой")
            print(f"Содержимое: {content}")
    except FileNotFoundError:
        print("Файл не найден")
    except EmptyFileError as e:
        print(e)

if __name__ == '__main__':
    # Создаем тестовые файлы
    with open('test.txt', 'w') as f:
        f.write("Есть данные")
    
    with open('empty.txt', 'w') as f:
        pass
    
    print("Файл с данными:")
    check_file('test.txt')
    
    print("\nПустой файл:")
    check_file('empty.txt')
    
    print("\nНесуществующий файл:")
    check_file('none.txt')
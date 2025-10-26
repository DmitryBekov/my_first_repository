import re

def load_banned_words(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        return content.lower().split()

def censor_text(text, banned_words):
    # Создаем регулярное выражение для каждого запрещенного слова
    for word in banned_words:
        # Ищем слово в любом регистре, даже как часть другого слова
        pattern = re.compile(re.escape(word), re.IGNORECASE)
        # Заменяем на звездочки той же длины
        replacement = '*' * len(word)
        text = pattern.sub(replacement, text)
    
    return text

def main():
    # Загружаем запрещенные слова
    banned_words = load_banned_words('input.txt')
    
    # Получаем текст от пользователя
    text = input("Введите предложение для проверки: ")
    
    # Цензурируем текст
    censored_text = censor_text(text, banned_words)
    
    print("Результат:")
    print(censored_text)

if __name__ == "__main__":
    main()
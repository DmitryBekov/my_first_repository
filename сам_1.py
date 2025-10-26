from collections import Counter
import re

def analyze_text(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
    
    # Разделение текста на слова (игнорируя знаки препинания)
    words = re.findall(r'\b\w+\b', text.lower())
    
    # Подсчет общего количества слов
    total_words = len(words)
    
    # Поиск самого частого слова
    word_counts = Counter(words)
    most_common_word, count = word_counts.most_common(1)[0]
    
    print(f"Общее количество слов: {total_words}")
    print(f"Самое частое слово: '{most_common_word}' (встречается {count} раз)")
    print(f"Топ-5 самых частых слов: {word_counts.most_common(5)}")

# Использование
analyze_text('статья.txt')
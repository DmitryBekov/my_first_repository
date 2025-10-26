def text_statistics(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    letter_count = 0
    word_count = 0
    line_count = len(lines)
    
    for line in lines:
        # Подсчет букв латинского алфавита
        for char in line:
            if char.isalpha() and char.isascii():
                letter_count += 1
        
        # Подсчет слов
        words = line.split()
        word_count += len(words)
    
    print(f"Input file contains:")
    print(f"{letter_count} letters")
    print(f"{word_count} words")
    print(f"{line_count} lines")

# Использование
text_statistics('input.txt')
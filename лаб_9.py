def find_longest_words(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        words = [line.strip() for line in file if line.strip()]
    
    if not words:
        return []
    
    max_length = max(len(word) for word in words)
    longest_words = [word for word in words if len(word) == max_length]
    
    return longest_words

result = find_longest_words('input.txt')
print("Слова с максимальной длиной:", result)
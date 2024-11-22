def count_words_in_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
            # Разделяем текст на слова
            words = text.split()
            return len(words)
    except FileNotFoundError:
        print(f"Файл '{filename}' не найден.")
        return 0


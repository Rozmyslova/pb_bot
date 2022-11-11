def reading_data():
    with open("phonebook.txt", "r", encoding='utf-8') as file:
        data = file.read()
        return data

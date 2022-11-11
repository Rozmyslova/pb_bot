def import_data_from_file():
    with open("for_import.txt", "r", encoding='utf-8') as file:
        data = file.read()
    export_file = open("phonebook.txt", "a", encoding='utf-8')
    export_file.write(data)
    export_file.close()

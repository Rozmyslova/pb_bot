def new_data(num, n_data):
    if num == 1:
        with open("phonebook.txt", "a", encoding='utf-8') as file:
            file.write(f'\n{n_data}')
    else:
        data = n_data.split(", ")
        with open("phonebook.txt", "a", encoding='utf-8') as file:
            file.write(f'\n{data[0]}, ')
        with open("phonebook.txt", "a", encoding='utf-8') as file:
            file.write(f'\n{data[1]}, ')
        with open("phonebook.txt", "a", encoding='utf-8') as file:
            file.write(f'\n{data[2]}, ')
            file.write('\n')

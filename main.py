import telebot
from telebot import TeleBot
from reading_data import reading_data
from new_data import new_data
from import_f import import_data_from_file



bot = TeleBot('5629323215:AAGtlxG0HBvfuhnMFKrSZllW58-_OA6lWek')


@bot.message_handler(commands=['start'])
def first_message(message):
    bot.send_message(message.chat.id,
                     text=(f'Это бот - телефонная книга. Список команд: \n'
                           '/start - запуск программы\n'
                           '/read - посмотреть телефонную книгу\n'
                           '/edit - ввести новые данные\n'
                           '/export - получить телефонную книгу в виде файла'))


@bot.message_handler(commands=['read'])
def bot_read_data(message):
    bot.send_message(message.chat.id, text=reading_data())
    bot.send_message(message.chat.id,
                     text=(f'Следующее действие: \n'
                           '/edit - ввести новые данные\n'
                           '/export - получить телефонную книгу в виде файла'))


@bot.message_handler(commands=['edit'])
def edit_one_line(message: telebot.types.Message):
    next_message = bot.send_message(chat_id=message.from_user.id, text='Укажите через запятую: ФИО, номер телефона, комментарий:' )
    bot.register_next_step_handler(callback=new_data_one, message=next_message)


def new_data_one(message):
    new_data(1, message.text)
    bot.send_message(message.chat.id,
                     text=(f'Следующее действие: \n'
                           '/read - посмотреть телефонную книгу\n'
                           '/export - получить справочник в виде файла'))


@bot.message_handler(commands=['start'])
def first_message(message):
    bot.send_message(message.chat.id,
                     text=(f'Следующее действие: \n'
                           '/read - посмотреть телефонную книгу\n'
                           '/export - получить справочник в виде файла'))


@bot.message_handler(content_types=['document'])
def bot_import_data(message: telebot.types.Message):
    file = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file.file_path)
    with open('for_import.txt', "w") as file_out:
        file_out.write(str(downloaded_file))
    import_data_from_file()
    bot.send_message(chat_id=message.from_user.id, text='Готово')


@bot.message_handler(commands=['export'])
def bot_export_data(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text='Сохранить в виде файла')
    bot.send_document(chat_id=msg.from_user.id, document=open('phonebook.txt', 'rb'))


bot.polling()

import telebot, Ethereum, threading, time, MongoDB
from datetime import datetime

bot = telebot.TeleBot('1204066865:AAEi1GKjnYGm5jM96sHuzjqarrHzdUB4nDo')


def timer_func():
    while True:
        for address in MongoDB.get_contracts_notification():
            notification = Ethereum.auction_event(address['Contract_Address'], address['Time'])
            if notification is not None:
                MongoDB.set_event_time(address['Contract_Address'], notification['Time'])
                MongoDB.contract_end(address,notification['Ended'])
                users = MongoDB.notification_all()
                for user in users:
                    bot.send_message(user, address['Date'] + ' ' + notification['Auction'])
            notification = Ethereum.bet_event(address['Contract_Address'], address['Buyer'])
            if notification is not None:
                MongoDB.set_event_time(address['Contract_Address'], address['Time'])
                MongoDB.contract_buyer(address, notification['Buyer'])
                users = MongoDB.notification_all()
                for user in users:
                    bot.send_message(user, address['Date'] + ' ' + notification['Bet'])
        time.sleep(30)

def start_menu():
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('Аукціони', 'Налаштування')
    return keyboard


def settings_menu():
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('Сповіщення', 'Надати доступ до гаманця', 'Видалити гаманець')
    keyboard.row('Стартове меню')
    return keyboard


def notificatins_menu():
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('Отримувати сповіщення', 'Не отримувати сповіщення')
    keyboard.row('Налаштування')
    return keyboard


def auction_menu():
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('Інформація про аукціон', 'Зробити ставку', 'Повернути кошти')
    keyboard.row('Стартове меню', 'Обрати аукціон', 'Підтвердити отримання')
    return keyboard


def admin_menu():
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('Обрати аукціон', 'Додати предмет', 'Додати смарт-контракт')
    keyboard.row('Почати аукціон', "Закінчити аукціон", 'Вивести кошти з контракту')
    return keyboard


@bot.message_handler(commands=['start'])
def send_welcome(message):
    board=start_menu()
    MongoDB.add_user(message.from_user.id)
    bot.send_message(message.from_user.id, "Привіт" + ' ' + str(message.from_user.last_name) + ' ' + str(message.from_user.first_name), reply_markup=board) #id = 462535778


@bot.message_handler(commands=['info'])
def send_welcome(message):
    bot.send_message(message.from_user.id, message)


@bot.message_handler(commands=['admin'])
def change_menu(message):
    if MongoDB.is_admin(message.from_user.id):
        board=admin_menu()
        bot.send_message(message.from_user.id, 'Вітаю адміністратор', reply_markup=board)
    else:
        bot.send_message(message.from_user.id, 'Ви не адміністратор')


@bot.message_handler(commands=['user'])
def change_menu(message):
    board=start_menu()
    bot.send_message(message.from_user.id, 'Стартове меню', reply_markup=board)


@bot.message_handler(content_types=["text"])
def Mess(message):
    if message.text == 'Інформація про аукціон':
        selected = MongoDB.get_selected_contract(message.from_user.id)
        if selected != 'Не обрано контракт':
            info = Ethereum.get_info(MongoDB.get_address_key(message.from_user.id), Ethereum.check(MongoDB.get_selected_contract(message.from_user.id)))
            mess ="Назва: " + info[0] + '\n' + 'Ціна: ' + str(info[1]) + '\n'
            if info[3] == 0:
                mess += 'Аукціон ще не розпочався' + '\n'
            else:
                mess += 'Аукціон розпочався: ' + datetime.fromtimestamp(info[3]).strftime("%d/%m/%y, %H:%M:%S") + '\n'
            if info[4] == 0:
                mess += 'Аукціон ще не закінчився' + '\n'
            else:
                mess += 'Аукціон закінчився: ' + datetime.fromtimestamp(info[4]).strftime("%d/%m/%y, %H:%M:%S") + '\n'
            if info[2] == 0:
                mess += 'Ви не робили ставок' + '\n'
            else:
                mess += 'Сума ваших ставок ставок' + str(info[2]) + '\n'
                if info[5] == MongoDB.get_address_key(message.from_user.id)['user_address']:
                    mess += 'Ваша ставка є переможною'
                else:
                    mess += 'Ви не лідуєте'
            bot.send_message(message.from_user.id, mess)
        else:
            bot.send_message(message.from_user.id, 'Аукціон не обрано')
    elif message.text == 'Додати смарт-контракт':
        if MongoDB.is_admin(message.from_user.id):
            contract = Ethereum.add_contact()
            MongoDB.add_conract(contract['Contract_Address'])
            bot.send_message(message.from_user.id, 'Геш транзакції: ' + str(contract['Tx_Hash']))
        else:
            bot.send_message(message.from_user.id, 'Ви не адміністратор')
    elif message.text == 'Вивести кошти з контракту':
        bot.send_message(message.from_user.id, Ethereum.withdraw(MongoDB.get_selected_contract(message.from_user.id)))
    elif message.text == 'Підтвердити отримання':
        user = MongoDB.get_address_key(message.from_user.id)
        if user is not None:
            if MongoDB.get_buyer(MongoDB.get_selected_contract(message.from_user.id)) == user['user_address']:
                bot.send_message(message.from_user.id, Ethereum.can_withdraw(MongoDB.get_selected_contract(message.from_user.id), user['user_address'], user['user_key']))
    elif message.text == 'Надати доступ до гаманця':
        MongoDB.set_user_query(message.from_user.id, 'user_address')
        bot.send_message(message.from_user.id, 'Адреса гаманця: ')
    elif message.text == 'Обрати аукціон':
        list = ''
        contracts=MongoDB.get_contracts()
        for i in range(0,len(contracts)):
            list = list + str(i+1) + '. '+ contracts[i] + '\n'
        MongoDB.set_user_query(message.from_user.id, 'set_contract')
        bot.send_message(message.from_user.id, 'Аукціони (вкажіть номер аукціону): \n' + list)
    elif message.text == 'Налаштування':
        board = settings_menu()
        bot.send_message(message.from_user.id, 'Меню налаштувань', reply_markup=board)
    elif message.text == 'Сповіщення':
        board = notificatins_menu()
        bot.send_message(message.from_user.id, 'Налаштування сповіщень', reply_markup=board)
    elif message.text == 'Аукціони':
        board = auction_menu()
        bot.send_message(message.from_user.id, 'Меню аукціонів', reply_markup=board)
    elif message.text == 'Додати предмет':
        if MongoDB.is_admin(message.from_user.id):
            MongoDB.set_user_query(message.from_user.id,'item_name')
            bot.send_message(message.from_user.id, 'Вкажіть назву предмету:')
        else:
            bot.send_message(message.from_user.id, 'Ви не адміністратор')
    elif message.text == 'Почати аукціон':
        if MongoDB.is_admin(message.from_user.id):
            bot.send_message(message.from_user.id, Ethereum.start_auction(MongoDB.get_selected_contract(message.from_user.id)))
        else:
            bot.send_message(message.from_user.id, 'Ви не адміністратор')
    elif message.text == 'Закінчити аукціон':
        if MongoDB.is_admin(message.from_user.id):
            bot.send_message(message.from_user.id, Ethereum.end_auction(MongoDB.get_selected_contract(message.from_user.id)))
        else:
            bot.send_message(message.from_user.id, 'Ви не адміністратор')
    elif message.text == 'Не отримувати сповіщення':
        MongoDB.not_notification(message.from_user.id)
        bot.send_message(message.from_user.id, 'Ви більше не отримуватимете сповіщення')
    elif message.text == 'Отримувати сповіщення':
        MongoDB.set_notification(message.from_user.id)
        bot.send_message(message.from_user.id, 'Ви будите отримувати сповіщення')
    elif message.text == 'Видалити гаманець':
        MongoDB.set_key(message.from_user.id, '')
        MongoDB.set_address(message.from_user.id, '')
        bot.send_message(message.from_user.id, 'Видалено')
    elif message.text == 'Повернути кошти':
        if MongoDB.get_address_key(message.from_user.id) is None or MongoDB.get_address_key(message.from_user.id)['user_address'] == '':
            bot.send_message(message.from_user.id, 'У нас немає вашого гаманця')
        else:
            address_key = MongoDB.get_address_key(message.from_user.id)
            bot.send_message(message.from_user.id, Ethereum.cash_back(MongoDB.get_selected_contract(message.from_user.id), address_key['user_address'],address_key['user_key']))
    elif message.text == 'Зробити ставку':
        if MongoDB.get_address_key(message.from_user.id) is None or MongoDB.get_address_key(message.from_user.id)['user_address'] == '':
            bot.send_message(message.from_user.id, 'У нас немає вашого гаманця')
        else:
            bot.send_message(message.from_user.id, 'Вкажіть суму ставки: ')
            MongoDB.set_user_query(message.from_user.id,'bet')
    elif message.text == 'Стартове меню':
        board = start_menu()
        bot.send_message(message.from_user.id, "Головне меню", reply_markup=board)
    elif MongoDB.get_user_query(message.from_user.id) != '':
        if MongoDB.get_user_query(message.from_user.id) == 'item_name':
            MongoDB.set_user_item(message.from_user.id, message.text)
            bot.send_message(message.from_user.id, 'Вкажіть ціну предмету:')
            MongoDB.set_user_query(message.from_user.id,'item_price')
        elif MongoDB.get_user_query(message.from_user.id) == 'item_price':
            MongoDB.set_user_query(message.from_user.id, '')
            hash = Ethereum.additem(MongoDB.get_selected_contract(message.from_user.id), MongoDB.get_user_item(message.from_user.id), int(message.text))
            MongoDB.set_user_item(message.from_user.id, '')
            bot.send_message(message.from_user.id, str(hash))
        elif MongoDB.get_user_query(message.from_user.id) == 'set_contract':
            MongoDB.set_user_query(message.from_user.id, '')
            if message.text.isdigit():
                MongoDB.set_selected_contract(message.from_user.id, MongoDB.get_contract_by_date(MongoDB.get_contracts()[int(message.text)-1]))
                bot.send_message(message.from_user.id, 'Обрано')
        elif MongoDB.get_user_query(message.from_user.id) == 'user_address':
            cheker = Ethereum.check(message.text)
            if cheker != 'Помилка, не правильно введено адресу':
                MongoDB.set_user_query(message.from_user.id, 'user_key')
                print(MongoDB.get_user_query(message.from_user.id) == 'user_key')
                MongoDB.set_address(message.from_user.id, Ethereum.check(message.text))
                bot.send_message(message.from_user.id, 'Ключ: ')
            else:
                MongoDB.set_user_query(message.from_user.id, '')
                bot.send_message(message.from_user.id, cheker)
        elif MongoDB.get_user_query(message.from_user.id) == 'user_key':
            MongoDB.set_user_query(message.from_user.id, '')
            MongoDB.set_key(message.from_user.id, message.text)
            bot.send_message(message.from_user.id, 'Виконано')
        elif MongoDB.get_user_query(message.from_user.id) == 'bet':
            MongoDB.set_user_query(message.from_user.id,'')
            address_key = MongoDB.get_address_key(message.from_user.id)
            selected = MongoDB.get_selected_contract(message.from_user.id)
            if address_key['user_address'] != '':
                bot.send_message(message.from_user.id, Ethereum.bet(selected, address_key['user_address'], address_key['user_key'], message.text))
            else:
                bot.send_message(message.from_user.id, 'у нас немає вашого гаманцю')
    else:
        bot.send_message(message.from_user.id, "Помилка, немає такої відповіді, спробуйте ще.")


if __name__ == '__main__':
    timer = threading.Thread(target=timer_func)
    timer.start()
    bot.polling(none_stop=True)

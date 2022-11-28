import telebot
from telebot import types

bot = telebot.TeleBot('5914667774:AAEstCwyiTPIrJkwFf5051XXIt7jk_dDwZg')

#контекстное меню со всеми командами
@bot.message_handler(commands=['start'])
def start(message):
    mess = f"Hello dear <b>{message.from_user.first_name}</b>, " \
           f"I do not know what wind brought you here! I can send you social networks and examples of my creator's work." \
           f" All you have to do is write a command!\n\n" \
           f"· Write /github and I will send you GitHub of my creator, where you can view his projects and works!\n" \
           f"· Write /linkedin and I will send you his LinkedIn, where can you contact him and see information about him!\n" \
           f"· Write /inst and I will send Instagram of my creatot, he is an aesthete, " \
           f"there you can look at beautiful pictures and photos!\n" \
           f"· Write /telega and I will send Telegram, you can write, ask how are you, he's quite friendly!\n" \
           f"· Write /vk and I will send VK, but he rarely sits there, but the music there is good!\n" \
           f"· Write /wechat and I will send his WeChat,there he also spends a lot of time communicating with " \
           f"Chinese people to improve his spoken Chinese!\n" \
           f"· Write /help if you suddenly forgot what I can do, although " \
           f"I already know that you have problems with your memory!\n"
    bot.send_message(message.chat.id, mess, parse_mode='html')

#описание всех команд
@bot.message_handler(commands=['github'])
def github(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("GitHub", url="https://github.com/MrSoulfinder"))
    bot.send_message(message.chat.id, 'You should check his GitHub! Right now! Thank YOU!', reply_markup=markup)


@bot.message_handler(commands=['linkedin'])
def linkedin(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("LinkedIn", url="https://www.linkedin.com/in/ilya-chernookiy-b5b42b258/"))
    bot.send_message(message.chat.id, 'Most likely he is now looking for a job, '
                                      'if you have something to offer him, you can contact him! Thank YOU!',
                     reply_markup=markup)


@bot.message_handler(commands=['inst'])
def inst(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Instagram", url="https://www.instagram.com/_just_miracle_/"))
    bot.send_message(message.chat.id, "This is his Instagram, it's pretty beautiful there! Rate and subscribe! "
                                      "Thanks!", reply_markup=markup)


@bot.message_handler(commands=['telega'])
def telega(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Telegram", url="https://t.me/bez_dushi"))
    bot.send_message(message.chat.id, "If you are sad or lonely, you can write to him, he likes to talk!", reply_markup=markup)


@bot.message_handler(commands=['vk'])
def vk(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("VK", url="https://vk.com/pupsoid341"))
    bot.send_message(message.chat.id, "This is his <b>VK</b>. If suddenly he doesn't answer for a long time, don't worry, "
                                      "he's probably programming!",parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['wechat'])
def wechat(message):
    photo = open('wechat.jpg','rb')
    bot.send_message(message.chat.id, "Wow, he also has <b>Wechat</b>. There he also spends a lot of time communicating with "
                                      "Chinese people to improve his spoken Chinese! Scan it!", parse_mode='html')
    bot.send_photo(message.chat.id,photo)

@bot.message_handler(commands=['help'])
def help(message):
    mess = f"<b>{message.from_user.first_name}</b>, I knew you'd forget something! start reading books " \
           f"and your memory will return to normal! Come on, don't be lazy! \n\n" \
           f"· Write /github and I will send you GitHub of my creator, where you can view his projects and works!\n" \
           f"· Write /linkedin and I will send you his LinkedIn, where can you contact him and see information about him!\n" \
           f"· Write /inst and I will send Instagram of my creatot, he is an aesthete, " \
           f"there you can look at beautiful pictures and photos!\n" \
           f"· Write /telega and I will send Telegram, you can write, ask how are you, he's quite friendly!\n" \
           f"· Write /vk and I will send VK, but he rarely sits there, but the music there is good!\n" \
           f"· Write /wechat and I will send his WeChat,there he also spends a lot of time communicating with " \
           f"Chinese people to improve his spoken Chinese!\n" \
           f"· Write /help if you suddenly forgot what I can do, although " \
           f"I already know that you have problems with your memory!"
    bot.send_message(message.chat.id, mess, parse_mode='html')


#работа с текстом
@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, "Admit it yourself took a picture or found it on the Internet, "
                                      "if by yourself, then handsome!It's all fun, but let's go through the teams better!")


@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text == "Hello" or message.text == "Hi" or message.text == "hello" or message.text == "hi":
        bot.send_message(message.chat.id, 'Wow, glad you are not dead yet!', parse_mode='html')
    elif message.text == "id" or message.text == "ID" or message.text == "Id":
        bot.send_message(message.chat.id, f'Your ID: {message.from_user.id}', parse_mode='html')
    elif message.text == "Photo" or message.text == "photo":
        photo = open('photo.jpg', 'rb')
        messtophoto = f'He looks something like this, maybe a little worse!'
        bot.send_message(message.chat.id, messtophoto, parse_mode='html')
        bot.send_photo(message.chat.id, photo)
    else:
        bot.send_message(message.chat.id, f'I do not understand you, '
                                          f'learn to talk like a human, please!', parse_mode='html')




bot.polling(none_stop=True)

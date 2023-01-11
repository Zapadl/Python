from telegram import Update, Bot ,InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters , CallbackQueryHandler
from credits import bot_token
import requests
from bs4 import BeautifulSoup as bs


bot = Bot(bot_token)
updater = Updater(bot_token, use_context=True)
dispatcher = updater.dispatcher
URL_TEMPLATE = "https://mixnews.lv/yumor"

def parse_url(url = URL_TEMPLATE):
    result_list = {'href': []}
    r = requests.get(url)
    soup = bs(r.text, "html.parser")
    url_post = soup.find_all("div",class_="post-item-normal one-posts")
    for name in url_post:
        result_list['href'].append(name.a['href'])
    return result_list
parse_url =str(parse_url())

def parse_post_title(url=URL_TEMPLATE):
    result_list = {'h4': []}
    r = requests.get(url)
    soup = bs(r.text, "html.parser")
    post_title = soup.find_all("h4")
    for name in post_title:
        result_list['h4'].append(name.text)
    return result_list
parse_t = str(parse_post_title())


def start(update, context):
    context.bot.send_message(update.effective_chat.id, "Привет!!  Давай спарсим сайт https://mixnews.lv/yumor")


def parse_button (update, context):
    keyboard = [
        [InlineKeyboardButton("Парсим url на сайте!!", callback_data="1")],
        [InlineKeyboardButton("Парсим заголовки  h4!!", callback_data="2")],
       ]
    update.message.reply_text("Выберите что будем делать?", reply_markup=InlineKeyboardMarkup(keyboard))

def button(update, context):
    query =update.callback_query
    query.answer()
    if query.data == "1":
           context.bot.send_message(update.effective_chat.id, parse_url)
    elif query.data == "2":
        context.bot.send_message(update.effective_chat.id, parse_t)



#Добавляем действиеб последовательно, сначала команды потом обработки текста
button_handler = CallbackQueryHandler(button)
start_handler = CommandHandler("start", start) #команды
parse_button_handler = CommandHandler("parse_button", parse_button ) #команды


#добавляем действия в сам телеграм бот
dispatcher.add_handler(start_handler)
dispatcher.add_handler(parse_button_handler)
dispatcher.add_handler(button_handler)


updater.start_polling()
updater.idle()
import telebot
#from . import config
import subprocess

bot = telebot.TeleBot('1731848821:AAGIPDkHG-mejUqZx-TBPdj-YAcED3RshbU')
'''
keyboard1=telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('EXMO')'''

@bot.message_handler(commands=['start'])
def start_messages(message):
    bot.send_message(message.chat.id, 'Привет, что хотите обменять?: ')

@bot.message_handler(content_types=['text'])
def echo(message):
    #bot.send_message(message.chat.id, "Боря гей")
    sum = message.text
    subprocess.run(["node", "index2.js", sum])
    #time.sleep(5)
    f1 = open("out2.txt", 'r')
    out = f1.read()
    f1.close()
    print(out)
    bot.send_message(message.chat.id, out)


'''
subprocess.run(["node", "myfirst/apps/pinatelonline/index.js", token_in])
#time.sleep(5)
f1 = open("myfirst/apps/pinatelonline/out.txt", 'r')
out = f1.read()
f1.close()
return HttpResponse(out)'''

bot.polling(none_stop=True)
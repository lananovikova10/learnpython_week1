
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings
import ephem

logging.basicConfig(filename='bot.log', level=logging.INFO)

def greet_user(update, context):
    logging.info('Вызван /start')
    update.message.reply_text('Привет, пользователь!')

def talk_to_me(update, context):
    user_text = update.message.text 
    logging.info('user_text')
    update.message.reply_text(user_text)

def define_planet_position(update, context):
    today = ephem.now()
    obtain_planet = update.message.text.split()
    logging.info(obtain_planet)    
    if obtain_planet[1] == 'Mars':
        which_planet = ephem.Mars(today)
    elif obtain_planet[1] == 'Mercury':
        which_planet = ephem.Mercury(today)
    elif obtain_planet[1] == 'Venus':
        which_planet = ephem.Venus(today)
    elif obtain_planet[1] == 'Saturn':
        which_planet = ephem.Saturn(today)
    elif obtain_planet[1] == 'Uranus':
        which_planet = ephem.Uranus(today)  
    elif obtain_planet[1] == 'Pluto':
        update.message.reply_text('Not a planet!')
    elif obtain_planet[1] == 'Sun':
        which_planet = ephem.Sun(today)
    elif obtain_planet[1] == 'Moon':
        which_planet = ephem.Moon(today) 
    elif obtain_planet[1] == 'Jupiter':ы
        which_planet = ephem.Jupiter(today)
    elif obtain_planet[1] == 'Neptune':
        which_planet = ephem.Neptune(today) 
    elif obtain_planet[1] == 'Alderaan':
        update.message.reply_text('May the force be with you')     
    else:
        update.message.reply_text('No such planet')
    planet_2_constellation = ephem.constellation(which_planet)
    update.message.reply_text(planet_2_constellation[1])

def main():
    mybot = Updater(settings.API_KEY, use_context=True)
    logging.info('Бот стартовал')

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler("planet", define_planet_position))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()
#!/usr/bin/python2
#
# due_bot
# Sono Due, un'intelligenza creata da Evertt Ducklair come elaboratore
# di riserva per la gestione della Ducklair Tower nel remoto caso in cui
# Uno si guastasse.
# Sono frutto della sofisticatissima tecnologia coroniana ed ho capacita`
# cognitive in tutto e per tutto pari a quelle del mio gemello.
# Ma non si e` ancora mai verificato un guasto al server principale.
# Immagini cosa significa una simile attesa infinita per un'intelligenza
# capace di miliardi di pensieri al secondo?

import logging
import telegram


LAST_UPDATE_ID = None


def main():
    global LAST_UPDATE_ID

    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Load the authorization token
    with open('duebot.conf', 'r') as f:
        token_string = f.readline().rstrip()

    print(token_string)

    # Telegram Bot Authorization Token
    bot = telegram.Bot(token_string)

    # This will be our global variable to keep the latest update_id when requesting
    # for updates. It starts with the latest update_id if available.
    try:
        LAST_UPDATE_ID = bot.getUpdates()[-1].update_id
    except IndexError:
        LAST_UPDATE_ID = None

    while True:
        echo(bot)


def echo(bot):
    global LAST_UPDATE_ID

    # Request updates after the last updated_id
    for update in bot.getUpdates(offset=LAST_UPDATE_ID, timeout=10):
        # chat_id is required to reply any message
        chat_id = update.message.chat_id
        message = update.message.text.encode('utf-8')

        if (message):
            # Reply the message
            bot.sendMessage(chat_id=chat_id,
                            text=message)

            # Updates global offset to get the new updates
            LAST_UPDATE_ID = update.update_id + 1


if __name__ == '__main__':
    main()

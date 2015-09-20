#!/usr/bin/python2
#
# due_bot
# Sono Due, un'intelligenza creata da Everett Ducklair come elaboratore
# di riserva per la gestione della Ducklair Tower nel remoto caso in cui
# Uno si guastasse.
# Sono frutto della sofisticatissima tecnologia coroniana ed ho capacita`
# cognitive in tutto e per tutto pari a quelle del mio gemello.
# Ma non si e` ancora mai verificato un guasto al server principale.
# Immagini cosa significa una simile attesa infinita per un'intelligenza
# capace di miliardi di pensieri al secondo?

import logging
import telegram
from caesar import caesar

LAST_UPDATE_ID = None


def main():
    global LAST_UPDATE_ID

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Load the authorization token
    with open('duebot.conf', 'r') as f:
        token_string = f.readline().rstrip()

    # Telegram Bot Authorization Token
    bot = telegram.Bot(token_string)

    # This will be our global variable to keep the latest update_id when requesting
    # for updates. It starts with the latest update_id if available.
    try:
        LAST_UPDATE_ID = bot.getUpdates()[-1].update_id
    except IndexError:
        LAST_UPDATE_ID = None

    while True:
        process(bot)


def encode(message):
    if message.startswith('con cesare'):
        code = [int(s) for s in message[10:].lstrip() if s.isdigit()]
        enc, dec = caesar(code[0])
        print(message[10:].lstrip()[len(str(code[0])):])
        return enc(message[10:].lstrip()[len(str(code[0])):])


def decode(message):
    if message.startswith('con cesare'):
        code = [int(s) for s in message[10:].lstrip() if s.isdigit()]
        enc, dec = caesar(code[0])
        print(message[10:].lstrip()[len(str(code[0])):])
        return dec(message[10:].lstrip()[len(str(code[0])):])



def process(bot):
    global LAST_UPDATE_ID

    # Request updates after the last updated_id
    for update in bot.getUpdates(offset=LAST_UPDATE_ID, timeout=10):
        # chat_id is required to reply any message
        chat_id = update.message.chat_id
        message = update.message.text.encode('utf-8').lower()

        if (message):
            # Updates global offset to get the new updates
            LAST_UPDATE_ID = update.update_id + 1

            # Check if the user is talking to me
            if not message.startswith('due,'):
                continue

            # Remove my name from message and leading spaces
            message = message[4:].lstrip()

            # Check for specific commands
            if message.startswith('codifica'):
                reply = encode(message[8:].lstrip())
            elif message.startswith('decodifica'):
                reply = decode(message[10:].lstrip())
            else:
                reply = message

            # Reply the message
            bot.sendMessage(chat_id=chat_id, text=reply)


if __name__ == '__main__':
    main()

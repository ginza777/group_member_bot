from django.core.management.base import BaseCommand
from telegram.utils.request import Request
from django.conf import settings
from  telegram import Bot
from telegram.ext import Updater
from bot_all.settings import TOKEN
from bot_function.bot_function import *
from bot_function.bot_members import *


#######

api_id='24990292'
api_hash="5cb886fc0d8c5d2ebe5d40ed6b50ab85"
from bot_all.settings import TOKEN
from telegram.ext import *
########


class Command(BaseCommand):
    help='Bu django telegram bot_function'

    def handle(self,*args,**options):
        request=Request(
        )
        bot=Bot(
            request=request,
            token=settings.TOKEN,


        )

        print(bot.get_me())


def handle_message(update, context):
    # Get basic info of the incoming message
    message_type = update.message.chat.type
    text = str(update.message.text).lower()
    response = ''

    # Print a log for debugging
    print(f'User ({update.message.chat.id}) says: "{text}" in: {message_type}')

    # React to group messages only if users mention the bot directly
    if message_type == 'group':
        # Replace with your bot username
        if '@geenza_bot' in text:
            new_text = text.replace('@geenza_bot', '').strip()
            response = handle_response(new_text)
    else:
        response = handle_response(text)

    # Reply normal if the message is in private
    update.message.reply_text(response)


# Log errors
def error(update, context):
    print(f'error caused error {context.error}')
# Run the program
# if __name__ == '__boot__':

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher

    # Commands
dp.add_handler(CommandHandler('start', start_command))
dp.add_handler(CommandHandler('help', help_command))
dp.add_handler(CommandHandler('custom', custom_command))
dp.add_handler(MessageHandler(Filters.regex("unfollow"), unfollow))
dp.add_handler(MessageHandler(Filters.regex("follow"), follow))
dp.add_handler(MessageHandler(Filters.status_update.new_chat_members, new_member))

dp.add_handler(MessageHandler(Filters.text, handle_message))
dp.add_error_handler(error)
updater.start_polling(1.0)
updater.idle()




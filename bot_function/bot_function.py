from botapp.management.commands.bot import *
from botapp.models import Profile
from telegram import ReplyKeyboardMarkup

print('Starting up bot_function...')

# Lets us use the /start command
def start_command(update, context):
    update.message.reply_text('Hello there! I\'m a bot_function. What\'s up?'
                              'follow my group @Geenza_officiall')
# Lets us use the /help command
def help_command(update, context):
    update.message.reply_text('Try typing anything and I will do my best to respond!')
# Lets us use the /custom command
def custom_command(update, context):
    update.message.reply_text('This is a custom command, you can add whatever text you want here.')


def handle_response(text) -> str:
    # Create your own response logic

    if 'hello' in text:
        return 'Hey there!'

    if 'how are you' in text:
        return 'I\'m good!'


    return text[::-1]


button=ReplyKeyboardMarkup([["follow",'unfollow']], resize_keyboard=True)

def follow(update, context):
    update.message.reply_text(f'Namaste {update.effective_user.first_name}',reply_markup=button)
    id = update.effective_user.id
    f_name = update.effective_user.first_name
    l_name = update.effective_user.last_name
    username = update.effective_user.username
    try:
        profile = Profile.objects.get(exeterenal_id=id)
        update.message.reply_text(f"siz bazada avalladan bor", reply_markup=button)
    except:
        Profile.objects.create(exeterenal_id=id, f_name=f_name, l_name=l_name, username=username)
        update.message.reply_text(f"bazaga qo'shildingiz", reply_markup=button)
def unfollow(update, context):
    update.message.reply_text(f'Namaste {update.effective_user.first_name}',reply_markup=button)
    id = update.effective_user.id
    f_name = update.effective_user.first_name
    l_name = update.effective_user.last_name
    username = update.effective_user.username
    try:
        profile = Profile.objects.get(exeterenal_id=id)
        profile.delete()
        update.message.reply_text(f"bazadan o'chirildingiz", reply_markup=button)
    except:

        update.message.reply_text(f"siz bazada kiritilmagansiz", reply_markup=button)





















#
# from botapp.models import Profile
# from telegram import Bot
# bot_function = Bot(TOKEN)
# button = ReplyKeyboardMarkup([["/start","follow",'unfollow','boshlash','adduser']], resize_keyboard=True)
#
#
#
#
# def hello(update, context):
#      update.message.reply_text(f'Hello {update.effective_user.first_name}',reply_markup=button)
#
#
# # //follow function ,if user not in database ,add user in database

#
#

#
# def boshlash(update, context):
#
#     chat_id = bot_function.get_chat("@Geenza_officiall").id
#     user_id = update.message.from_user.id
#
#     # Get the ChatMember object for the user in the channel
#     chat_member = context.bot_function.get_chat_member(chat_id, user_id)
#
#     # Check if the user is following the channel
#     if chat_member.status == "member":
#         update.message.reply_text("You are following the channel!")
#     else:
#         update.message.reply_text("You are not following TO @Geenza_official the channel.")
# def adduser(update, context):
#     chat_id = bot_function.get_chat("@Geenza_officiall").id
#     user_id = update.message.from_user.id
#     print("chat_id: ",chat_id)
#     print("user_id: ",user_id)
#
#     # Check if the user is currently a member of the group or channel //user status
#     # chat_member = bot_function.get_chat_member(chat_id, user_id)
#     # if chat_member.status == 'member':
#     #     print('User is currently a member')
#     # elif chat_member.status == 'left':
#     #     print('User has left the group or channel')
#     # elif chat_member.status == 'kicked':
#     #     print('User has been kicked from the group or channel')
#     # else:
#     #     print('User status is unknown')
#     ###################################
#
#
#
#     member_count = bot_function.get_chat_members_count(chat_id)
#
#     # Print member count
#     print('Number of members:', member_count)
#
#     # Get the user who added the new member
#     user = update.message.from_user
#     # Get the new members
#     new_members = update.message.new_chat_members
#         # Print the username of the user who added the new member
#     print(f'{user.username} added {len(new_members)} new members')
#     update.message.reply_text(f'{user.username} added {len(new_members)} new members to @Geenza_officiall')
#         # Print the usernames of the new members
#     for member in new_members:
#         print(member.username)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# updater = Updater(TOKEN)
# dp = updater.dispatcher
# dp.add_handler(CommandHandler("start", hello))

# dp.add_handler(MessageHandler(Filters.regex("boshlash"), boshlash))
# dp.add_handler(MessageHandler(Filters.regex("adduser"), adduser))
# updater.start_polling()
# updater.idle()
#
# # import time
# # from bot_all.settings import TOKEN,api_id,api_hash,group_chat_id
# #
# # from telethon import TelegramClient
# # from telethon.tl.functions.channels import GetParticipantsRequest
# # from telethon.tl.types import ChannelParticipantsSearch
# # from telethon.errors.rpcerrorlist import PeerFloodError
# #
# # # Replace YOUR_API_ID and YOUR_API_HASH with your own API credentials
# #
# #
# # client = TelegramClient('session_name', api_id, api_hash)
# #
# # # Replace GROUP_CHAT_ID with the ID of the group you want to get the members of
# #
# #
# # async def get_all_members():
# #     all_participants = []
# #     filter_entity = ChannelParticipantsSearch('')
# #     try:
# #         participants = await client(GetParticipantsRequest(channel=group_chat_id,
# #                                                             filter=filter_entity,
# #                                                             offset=0,
# #                                                             limit=100,
# #                                                             hash=0))
# #         all_participants.extend(participants.users)
# #     except PeerFloodError:
# #         print("Getting too many participants too fast. Sleeping for 5 seconds...")
# #         time.sleep(5)
# #     except Exception as e:
# #         print("Exception:", e)
# #
# #     return all_participants
# #
# # with client:
# #     all_members = client.loop.run_until_complete(get_all_members())
# #     for member in all_members:
# #         print(member.first_name,member.access_hash)
# #
#

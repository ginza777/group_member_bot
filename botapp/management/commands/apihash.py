TOKEN="5612140723:AAGZvc3Tjay95-3qAZ0V44cU42SL5X93PT8"
group_chat_id =-1001685288972
api_id='24990292'
api_hash="5cb886fc0d8c5d2ebe5d40ed6b50ab85"
from botapp.models import Group_members_api
import time
from bot_all.settings import TOKEN,api_id,api_hash,group_chat_id


from django.core.management.base import BaseCommand
from telegram.utils.request import Request
from django.conf import settings
from  telegram import Bot



class Command(BaseCommand):
    help='Bu django telegram bot_function'

    def handle(self,*args,**options):
        request=Request(
        )








from telethon import TelegramClient
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch
from telethon.errors.rpcerrorlist import PeerFloodError

# Replace YOUR_API_ID and YOUR_API_HASH with your own API credentials


client = TelegramClient('session_name', api_id, api_hash)




async def get_all_members():
    all_participants = []
    filter_entity = ChannelParticipantsSearch('')
    try:
        participants = await client(GetParticipantsRequest(channel=group_chat_id,
                                                            filter=filter_entity,
                                                            offset=0,
                                                            limit=100,
                                                            hash=0))
        all_participants.extend(participants.users)
    except PeerFloodError:
        print("Getting too many participants too fast. Sleeping for 5 seconds...")
        time.sleep(5)
    except Exception as e:
        print("Exception:", e)

    return all_participants


with client:
    all_members = client.loop.run_until_complete(get_all_members())
    for member in all_members:


        try:


            user=Group_members_api.objects.get(exeterenal_id=member.id)
            print(f'user is exist: {member.id}')
            group_id=group_chat_id
            user.contact=member.contact
            user.phone=member.phone
            user.premium=member.premium
            user.bot=member.bot
            user.lang_code=member.lang_code
            user.username=member.username
            user.f_name=member.first_name
            user.l_name=member.last_name
            user.save()

        except:
              print(f"user is not exist: {member.id}")
              Group_members_api.objects.create(group_id=group_chat_id,exeterenal_id=member.id,contact=member.contact,phone=member.phone,premium=member.premium,bot=member.bot,lang_code=member.lang_code,username=member.username,f_name=member.first_name,l_name=member.last_name)


























































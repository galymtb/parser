from telethon import TelegramClient
from telethon.errors.rpcerrorlist import PeerFloodError
import sys
import time

api_id = '3847679'
api_hash = '203eae28a3a7012a727c92e1f0a209ca'
client = TelegramClient('my_account', api_id, api_hash)

cht_fbc = 'tutors24edufbc'
cht_sat = 'tutors24edusat'
cht_edu = 'tutors24edu'
fbc = []
sat = []
edu = []
all = []

async def getter():
    participants = await client.get_participants(cht_fbc, aggressive=True)
    for user in participants:
        if user.id is not None:
            fbc.append(user.username)

    participants = await client.get_participants(cht_sat)
    for user in participants:
        if user.id is not None:
            sat.append(user.username)

    participants = await client.get_participants(cht_edu)
    for user in participants:
        if user.id is not None:
            edu.append(user.username)

    all = set(fbc)
    SLEEP_TIME = 15
    for user.username in all:
        try:
            print("Sending Message to:", user.username)
            await client.send_message(user.username, '❗️Reminder\n'
                                                     'Напоминаем, что сегодня в 18:00 (Нур-Султан, GMT+06) наш ментор Айдар Айдралиев будет проводить вебинар-презентацию курса по поступлению в США🇺🇸 \n'
                                                     '\n'
                                                     'Также, в конце он проведёт Q&A сессию и ответит на Ваши вопросы!\n'
                                                     '\n'
                                                     'Ссылка на участие будет опубликована в нашем Telegram канале:\n'
                                                     'https://t.me/tutors24edufbc')
            print("Waiting {} seconds".format(SLEEP_TIME))
            time.sleep(SLEEP_TIME)
        except PeerFloodError:
            print("Getting Flood Error from telegram. Script is stopping now. Please try again after some time.")
            sys.exit()
        except Exception as e:
            print("Error:", e)
            print("Trying to continue...")
        continue

    print(all)
    print(len(all))

with client:
    client.loop.run_until_complete(getter())


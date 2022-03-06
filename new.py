from telethon import TelegramClient
api_id = '3115692'
api_hash = '6ff5cc00898a5992262ab44c9ddc4318'
client = TelegramClient('my_account', api_id, api_hash)
 
chtid = tutors24edufbc
clean_usernames = []
 
async def getter():
    participants = await client.get_participants(chtid)
    for user in participants:
        if user.id is not None:
            clean_usernames.append(user.id)
    print(clean_usernames)
 
with client:
    client.loop.run_until_complete(getter())
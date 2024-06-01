from telethon import TelegramClient, events

# Your API credentials
api_id = '25810549'
api_hash = '695283c8b7c61e2c9726e1b2a5f3beb7'
bot_token = '7492683084:AAEQ-SnTtxtvpG6kIB1GPJDX7-y40rHMa8w'

client = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

@client.on(events.NewMessage)
async def handler(event):
    sender = await event.get_sender()
    print(f'Chat ID: {sender.id}')

client.run_until_disconnected()

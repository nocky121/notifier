from telethon import TelegramClient, events
import requests
import os

# Define your API ID, API hash, and bot token
api_id = '25810549'
api_hash = '695283c8b7c61e2c9726e1b2a5f3beb7'
bot_token = '7492683084:AAEQ-SnTtxtvpG6kIB1GPJDX7-y40rHMa8w'
# Replace with your bot chat ID
bot_chat_id = '6735950714'
# Numbers to monitor
TARGET_NUMBERS = {24, 72, 216, 648, 1944}
# Channel to monitor
channel_username = 'lottery_9_7'

# Use a unique session name for each instance
session_name = os.environ.get('SESSION_NAME', 'session')

# Create a Telegram client with the unique session name
client = TelegramClient(session_name, api_id, api_hash)

# Define the function to send a message to your bot
def send_message_to_bot(text):
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    data = {
        'chat_id': bot_chat_id,
        'text': text
    }
    requests.post(url, data=data)

# Event handler for new messages
@client.on(events.NewMessage(chats=channel_username))
async def my_event_handler(event):
    message_text = event.message.message
    if any(str(num) in message_text for num in TARGET_NUMBERS):
        message_link = f'https://t.me/{channel_username}/{event.message.id}'
        alert_text = f"Alert: Found message with target number(s) - {message_link}"
        send_message_to_bot(alert_text)

# Start the client
async def main():
    await client.start()
    print('Monitoring started...')
    await client.run_until_disconnected()

# Run the main coroutine
if __name__ == '__main__':
    import asyncio
    asyncio.run(main())

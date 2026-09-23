import os
from telethon import TelegramClient, events

api_id = int(os.environ["API_ID"])
api_hash = os.environ["API_HASH"]

SOURCE_CHANNEL = int(os.environ["SOURCE_CHANNEL"])
DESTINATION_GROUP = int(os.environ["DESTINATION_GROUP"])

KEYWORD = "Ashey"
REPLACEMENT = "Nayan Amit"

client = TelegramClient("forwarder_session", api_id, api_hash)


@client.on(events.NewMessage(chats=SOURCE_CHANNEL))
async def handler(event):
    message = event.message
    text = message.text or ""

    if KEYWORD.lower() not in text.lower():
        return

    new_text = text.replace(KEYWORD, REPLACEMENT)

    if message.media:
        await client.send_file(
            DESTINATION_GROUP,
            message.media,
            caption=new_text
        )
    else:
        await client.send_message(
            DESTINATION_GROUP,
            new_text
        )

    print("Copied:", new_text)


print("Forwarder is running...")
client.start()
client.run_until_disconnected()

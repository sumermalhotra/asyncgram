# Telegram requirements

To be able to use this tool, you will require a Telegram bot token and a group chat ID. 

[Telegram bot token reference](https://core.telegram.org/bots#6-botfather)

[Telegram group chat ID reference](https://stackoverflow.com/questions/32423837/telegram-bot-how-to-get-a-group-chat-id)

# Installation

```
pip install asyncgram
```

# Usage

Once you have your telegram bot token and group chat ID, and you've install asyncgram, you are ready to get started. 

## Creating a client

```
from asyncgram import Asyncgram

# replace XXX with your keys
TG_BOT_TOKEN = "XXX"
TG_GROUP_ID = "XXX"

client = Asyncgram(
    tg_token = TG_BOT_TOKEN, 
    tg_group = TG_GROUP_ID
)
```

## Logging messages

```
client.start()

messages = [
    'Hello world',
    'My name is codeman',
    'My birthday was yesterday.'
]

for msg in messages: client.put(msg)

client.stop()
```

This is a toy example to get you started. Recommended usage would be to put relevant messages from some form of a websocket connection such that it's logged in an asynchronous way.
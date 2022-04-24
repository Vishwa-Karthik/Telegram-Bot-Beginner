# Telegram-Bot-Beginner Tutorial
#### A Beginner's roadmap to develop Telegram Bot using Python

## Installation 
1. Use the package manager [pip](https://pip.pypa.io/en/stable/) to install PyTelegramBotAPI.

```bash
pip install PyTelegramBotAPI
```

2. Use the package manager [pip](https://pip.pypa.io/en/stable/) to install telebot.

```bash
pip install telebot
```
## Pre-Reqs
### Open Telegram and Search for [BotFather](https://telegram.me/BotFather)
#### -> We now presume you have obtained API key. We will call this "Token".

## Usage
  
```python
import telebot

TOKEN = '<token string>'

tb = telebot.TeleBot(TOKEN)
```
  We need to register some so-called message handlers. Message handlers define filters which a message must pass. If a message passes the filter, the decorated function is called and the incoming message is passed as an argument.

Let's define a message handler which handles incoming /start and /greet commands.
```python
@bot.message_handler(commands=['Start', 'Greet'])
def start(message):
	tb.reply_to(message, "Hya, Greetings !!\nType Help")
 ```
  

```python
#sendMessage
@bot.message_handler(commands=["commandName"])
def foofoo(message):
    tb.send_message(chatid, text)
```
### Similarly

```python
# forwardMessage
tb.forward_message(to_chat_id, from_chat_id, message_id)

# sendPhoto
photo = open('/tmp/photo.png', 'rb')
tb.send_photo(chat_id, photo)
file_id = 'pic1'
tb.send_photo(chat_id, file_id)

# sendAudio
audio = open('/tmp/audio.ogg', 'rb')
tb.send_audio(chat_id, audio)
file_id = 'aud1'
tb.send_audio(chat_id, file_id)

# sendDocument
doc = open('/tmp/file.txt', 'rb')
tb.send_document(chat_id, doc)
file_id = 'doc1'
tb.send_document(chat_id, file_id)

# sendLocation
tb.send_location(chat_id, lat, lon)
```
## We now need to add a listener function to accept request from Telegram
```python
while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(5)
```

### To further explore package, please refer to the [PyTelegramBotAPI package](https://pypi.org/project/pyTelegramBotAPI/0.3.0/).

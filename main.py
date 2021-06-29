import requests
import os
from telegram.ext import Updater, MessageHandler, Filters


Token = ">>>>Token<<<<<"

def python_file(update, context):
    file = context.bot.getFile(update.message.document.file_id)
    fileName = update.message.document.file_name
    path = os.path.splitext(fileName)[1]
    if path == ".py":
        file.download(fileName)

        with open(fileName, "r", encoding="utf-8") as file:
            a = file.read()
            data = {
                "poster": fileName,
                "syntax": "python3",
                "expiration": "year",
                "content": a,
            }
            chat_id = update.message.chat_id
            message_id = update.message.message_id
            url = requests.post("https://paste.ubuntu.com", data=data).url

            message_ = f"""
    ✷✷✷ Dosya Başarılı bir şekilde  yüklendi ✷✷✷
    
➾ Dosya İsmi : {fileName}

➾ Paste Ubuntu linki : {url} 

            
            """
            update.message.reply_text(message_)

            requests.post(f"https://api.telegram.org/bot{Token}/deleteMessage?chat_id={chat_id}&message_id={message_id}")


def main():

    updater = Updater(Token, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(MessageHandler(Filters.document, python_file))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
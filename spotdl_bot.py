import shutil

import telebot

from spotify_api import *

bot_token = "5883531168:AAGEQgKG5KeP9BHxfm3o052XW4Ovoj3-2CM"
links = []


# def upload_files_in_a_folder_to_bot(path: str, bot_token: str, chat_id: str, title: str):
#     send_message_to_telegram_bot(bot_token=bot_token, bot_chatId=chat_id, message=title)
#     for root, dirs, files in os.walk(path):
#         for file in files:
#             if file.endswith(".mp3"):
#                 send_audio_to_telegram_bot(bot_token=bot_token, bot_chatId=chat_id,
#                                            file_with_path=os.path.join(root, file))


def upload_files_in_a_folder_to_bot_bot_input(path: str, chat_id: str, bot: telebot.TeleBot):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".mp3"):
                audio = open(os.path.join(root, file), 'rb')
                bot.send_audio(chat_id=chat_id, audio=audio)


if __name__ == "__main__":
    try:
        shutil.rmtree("./sp")
    except FileNotFoundError:
        pass
    for link in links.copy():
        cmd = f"spotifydl {link} --o ./sp"
        os.system(cmd)
        id = link[link.rfind("/") + 1:]
        name = get_album_name(album_id=id)
        # upload_files_in_a_folder_to_bot(bot_token=bot_token, chat_id="1072294373", path="./sp", title=name)
        try:
            shutil.rmtree("./sp")
        except:
            print("e")
        links.remove(link)
        print(links)

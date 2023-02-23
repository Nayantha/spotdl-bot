import logging
import os

import telebot

from spotdl_bot import upload_files_in_a_folder_to_bot_bot_input
from spotify_api import get_name_from_link

if __name__ == '__main__':
    os.system("npm install -g spotify-dl")
    
    bot_name: str = ""
    bot_token = os.getenv("BOT_TOKEN")
    bot_chatId = os.getenv("BOT_CHAT_ID")
    logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
    logging.info("Starting bot")
    
    bot = telebot.TeleBot(token=bot_token, parse_mode=None)
    
    
    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        bot.reply_to(message, "Howdy, how are you doing?")
    
    
    @bot.message_handler(regexp="spotify")
    def handle_message(message):
        dwn_path = "./sp"
        
        link = message.text
        cmd = f"spotifydl {link} --o  {dwn_path}"
        os.system(cmd)
        name = get_name_from_link(link=link)
        bot.reply_to(message, f"{name} downloading...")
        
        upload_files_in_a_folder_to_bot_bot_input(bot=bot, path=dwn_path, chat_id=bot_chatId)
        
        # https://open.spotify.com/album/4EL83JlSoVsYWbqLJIlxSv?highlight=spotify:track:0i9BCUg1LP9Z0dcRd76bcD
        # https://open.spotify.com/track/0i9BCUg1LP9Z0dcRd76bcD
    
    bot.infinity_polling()
    
    
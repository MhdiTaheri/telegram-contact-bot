import telebot
from googletrans import Translator, LANGUAGES

BOT_TOKEN = 'BOT_TOKEN'
ADMIN_CHAT_ID = ADMIN_CHAT_ID

bot = telebot.TeleBot(BOT_TOKEN)
translator = Translator()
user_languages = {}

def is_valid_language_code(code):
    return code in LANGUAGES

language_commands = {
    'language': 'en',
    'jezik': 'hr',
    'زبان': 'fa',
}

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.chat.id
    user_lang = user_languages.get(user_id, 'en')
    welcome_message = translate_message('Welcome! Please set your preferred language by sending a message like this: /language en', user_lang)
    bot.reply_to(message, welcome_message)

@bot.message_handler(func=lambda message: message.text and message.text.split()[0][1:] in language_commands)
def set_language(message):
    command = message.text.split()[0][1:]
    lang_code = language_commands[command]
    
    try:
        user_input = message.text.split()[1]
        if is_valid_language_code(user_input):
            user_languages[message.chat.id] = user_input
            response_message = translate_message(f'Language set to {user_input}.', user_input)
            bot.reply_to(message, response_message)
        else:
            invalid_message = translate_message('Invalid language code. Please see valid language codes here: https://cloud.google.com/translate/docs/languages', lang_code)
            bot.reply_to(message, invalid_message)
    except IndexError:
        invalid_format_message = translate_message('Please provide a language code. Example: /language en', lang_code)
        bot.reply_to(message, invalid_format_message)

def translate_message(text, dest):
    try:
        translated = translator.translate(text, dest=dest)
        return translated.text
    except Exception as e:
        return f"Error in translation: {e}"

@bot.message_handler(func=lambda message: True, content_types=['text', 'sticker', 'photo', 'video', 'document', 'audio'])
def forward_message(message):
    user_id = message.chat.id
    user_lang = user_languages.get(user_id, 'en')
    
    if user_id != ADMIN_CHAT_ID:
        if message.content_type == 'text':
            translated_text = translate_message(message.text, 'en')
            forward_text = f'New message from @{message.from_user.username} (ID: {message.from_user.id}):\n{translated_text}'
            bot.send_message(ADMIN_CHAT_ID, forward_text)
        elif message.content_type == 'sticker':
            bot.send_message(ADMIN_CHAT_ID, f'New sticker from @{message.from_user.username} (ID: {message.from_user.id}):')
            bot.forward_message(ADMIN_CHAT_ID, user_id, message.message_id)
        else:
            bot.send_message(ADMIN_CHAT_ID, f'New {message.content_type} from @{message.from_user.username} (ID: {message.from_user.id}):')
            bot.forward_message(ADMIN_CHAT_ID, user_id, message.message_id)
        
        reply_text = translate_message('Your message has been forwarded to the admin.', user_lang)
        bot.reply_to(message, reply_text)
    else:
        try:
            parts = message.text.split(' ', 1)
            if len(parts) != 2:
                raise ValueError('Invalid format. Please use: [user_chat_id] [reply_message]')
            
            user_chat_id = int(parts[0])
            reply_text = parts[1]
            
            user_lang = user_languages.get(user_chat_id, 'en')
            translated_reply = translate_message(reply_text, user_lang)
            
            bot.send_message(user_chat_id, translated_reply)
            bot.send_message(ADMIN_CHAT_ID, 'Reply sent successfully.')
        except ValueError as e:
            bot.reply_to(message, str(e))
        except Exception as e:
            bot.reply_to(message, f'An error occurred: {str(e)}')

bot.polling()

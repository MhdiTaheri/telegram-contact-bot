
# 🤖 Telegram Bot with Language Translation 🌐

[![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This is a fun and interactive Telegram bot that forwards messages to an admin and translates them into English. It also allows users to set their preferred language and reply to users in their preferred language.

## 📋 Features

- 📨 Forwards messages to an admin
- 🌐 Translates messages into English
- 🌟 Allows users to set their preferred language
- 💬 Allows admin to reply to users in their preferred language
- 📝 Provides a user-friendly interface with emojis and inline keyboard markup
- 📝 Includes a welcome message, language selection message, confirmation message, goodbye message, and fallback message
- 📝 Includes a help message that lists all available commands and their usage
- 📝 Includes a feedback mechanism that allows users to provide feedback or report issues
- 📝 Uses a consistent layout and design for messages
- 📝 Includes a loading indicator that shows when the bot is processing a request
- 📝 Uses a caching mechanism that stores user preferences and translations to improve performance and reduce the number of requests to the translation API

## 📝 Prerequisites

-  Python 3.6 or higher
-  Telegram Bot Token
-  Admin Chat ID

## 💻 Installation

1. 📥 Clone the repository:

   ```
   git clone https://github.com/DevSeyed/telegram-contact-bot.git
   ```

2. 📁 Navigate to the project directory:

   ```
   cd telegram-contact-bot
   ```

3. 📦 Install the required Python packages:

   ```
   pip install -r requirements.txt
   ```

4. 🔄 Replace `BOT_TOKEN` and `ADMIN_CHAT_ID` in the script with your own Telegram Bot Token and Admin Chat ID.

## 🚀 Usage

1. 💻 Run the script:

   ```
   python bot.py
   ```

2. 💬 Start a conversation with your bot on Telegram.

3. 🌐 Use the inline keyboard markup to set your preferred language.

4. 📨 Send a message to the bot. The bot will forward the translated message to the admin.

5. 💬 To reply to a user, send a message to the bot in the format `[user_chat_id] [reply_message]`. For example, `123456789 Hello, how are you?` to reply to the user with chat ID 123456789.

6. 📝 Use the `/help` command to view a list of available commands and their usage.

7. 📝 Use the feedback mechanism to provide feedback or report issues.

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## 📜 License

[MIT](https://choosealicense.com/licenses/mit/)

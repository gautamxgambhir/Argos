<div align="center">
  <img src="https://i.ibb.co/ZpLTY3CS/argos.png" alt="Argos Logo"><br>
</div>

-----------------

# Argos: AI-Powered Debate Bot for Telegram & Discord

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Flask](https://img.shields.io/badge/Flask-2.0-green)
![Status](https://img.shields.io/badge/status-active-brightgreen)
![License](https://img.shields.io/badge/license-MIT-red)
![Together-AI](https://img.shields.io/badge/Together%20AI-0f6fff)
![Telegram](https://img.shields.io/badge/Telegram-Bot-blue)
![Discord](https://img.shields.io/badge/Discord-Bot-purple)

## What is Argos?

Argos is an AI-powered **debate bot** for **Telegram & Discord** that challenges users on any topic by taking the opposing stance. Whether you argue **in favor** or **against** a subject, Argos will always take the opposite position, ensuring a balanced and thought-provoking discussion.

## Features

- **Opposing Debate Stance**: If you argue *in favor* of a topic, Argos will argue *against* it, and vice versa.
- **Supports Telegram & Discord**: Available as both a **Telegram bot** and a **Discord bot**.
- **AI-Powered Responses**: Uses **Together API** to generate intelligent counterarguments.
- **Fast & Dynamic**: Provides quick responses to keep the debate engaging.
- **Customizable Prefix for Discord**: Uses `!` as the default prefix for Discord commands.

## Bot Descriptions

### **Discord Bot Description**
*Just use commands like !start, !stop, and !dm to begin or end a debate session. A*

### **Telegram Bot Description**
*Start with /start, chat in DM with /dm, and end with /stop.*

## Where to Access It?

Argos is open-source and available on GitHub:

🔗 **[GitHub Repository](https://github.com/gautamxgambhir/Argos)**

### **Invite & Use the Bot**

- **Telegram Bot**: [@ArgosDebateBot](https://t.me/ArgosDebateBot)
- **Discord Bot Invite**: [Invite Argos to Your Server](https://discord.com/oauth2/authorize?client_id=1321105115012403331&permissions=8&integration_type=0&scope=bot)

## Installation and Setup

### 1. Clone the repository:
```bash
 git clone https://github.com/gautamxgambhir/Argos.git
```

### 2. Install dependencies:
```bash
cd Argos
pip install -r requirements.txt
```

### 3. Set up API keys
- Obtain a **Together AI API Key** from [Together AI](https://www.together.ai/).
- Set up **Telegram Bot Token** via [BotFather](https://core.telegram.org/bots#botfather).
- Set up **Discord Bot Token** via the [Discord Developer Portal](https://discord.com/developers/applications).
- Store the API keys in an **.env** file:
```env
API_KEY=your_together_api_key
TELEGRAM_TOKEN=your_telegram_bot_token
DISCORD_TOKEN=your_discord_bot_token
```

### 4. Run the bot:
```bash
python bot.py
```

## Discord Bot Usage

- **Prefix**: `!`
- **Example Commands**:
  - `!start` → Debate session started.
  - `Climate change is real.` → Type your arguments. Argos will argue the opposing side.
  - `!stop` → Stop the debate session.
  - `!dm` → To debate in Direct Message.

## Telegram Bot Usage

- Simply **send a statement**, and Argos will respond with an opposing viewpoint.
- **Commands**:
  - `/start` → Start a debate session.
  - `Climate change is real.` → Type your arguments. Argos will argue the opposing side.
  - `/dm` → Chat in direct messages.
  - `/stop` → End the debate session.

## Dependencies

- [**Flask**](https://flask.palletsprojects.com/en/3.0.x/) - Backend framework for API integration.
- [**Together API**](https://www.together.ai/) - AI-powered debate response generation.
- [**python-telegram-bot**](https://python-telegram-bot.readthedocs.io/) - Telegram bot framework.
- [**discord.py**](https://discordpy.readthedocs.io/en/stable/) - Discord bot framework.

## Contributing

Contributions are welcome! To contribute:
- Fork the repo.
- Create a new branch (`git checkout -b feature-branch`).
- Commit changes (`git commit -m "Added new feature"`).
- Push to the branch (`git push origin feature-branch`).
- Open a pull request.

## License

This project is licensed under the **MIT License**.

## Contact

- **GitHub**: [@gautamxgambhir](https://github.com/gautamxgambhir)
- **Email**: ggambhir1919@gmail.com
- **Instagram**: [gautamxgambhir](https://www.instagram.com/gautamxgambhir)
- **Twitter**: [gautamxgambhir](https://www.twitter.com/gautamxgambhir)
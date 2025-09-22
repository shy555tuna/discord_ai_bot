# Guide to Setting Up a Discord AI Bot on Windows and Linux

This guide walks you through setting up a Discord bot that uses Google's Gemini AI to chat. It works on both Windows and Linux systems.

## Prerequisites

- A Discord account and a server where you have permission to add bots.
- A Google Cloud account to obtain a Gemini API key.
- Python 3.8 or newer installed on your system.
- A text editor (e.g., VS Code, Notepad++, Sublime Text).

## Step 1: Obtain Your API Keys

### Discord Bot Token
1. Visit the [Discord Developer Portal](https://discord.com/developers/applications).
2. Create a new application and give it a name.
3. Go to the "Bot" tab and click "Add Bot."
4. Copy the bot token and store it securely.
5. To add the bot to your server:
   - Go to "OAuth2" -> "URL Generator" in the Discord Developer Portal.
   - Select the `bot` scope.
   - Choose permissions: `Send Messages` and `Read Messages/View Channels`.
   - Copy the generated URL, open it in a browser, and invite the bot to your server.

### Google Gemini API Key
1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project or select an existing one.
3. Enable the "Generative AI API" for your project.
4. Navigate to "APIs & Services" -> "Credentials" and create an API key.
5. Copy the API key and keep it secure.

## Step 2: Set Up Your Environment

### On Windows
1. **Install Python**:
   - Download Python 3.8 or newer from [python.org](https://www.python.org/downloads/).
   - Run the installer and ensure "Add Python to PATH" is checked.
   - Verify installation by opening Command Prompt and running:
     ```
     python --version
     ```
2. **Install Required Packages**:
   - In Command Prompt, install the necessary libraries:
     ```
     pip install discord.py google-generativeai
     ```
3. **Create a Project Folder**:
   - Create a folder (e.g., `DiscordAIBot`) on your computer.
   - Save the provided `discord_ai_bot.py` code as `discord_ai_bot.py` in this folder.

### On Linux
1. **Check for Python**:
   - Most Linux distributions include Python. Verify with:
     ```
     python3 --version
     ```
   - If not installed, use your package manager:
     - **Ubuntu/Debian**:
       ```
       sudo apt update && sudo apt install python3 python3-pip
       ```
     - **Fedora**:
       ```
       sudo dnf install python3 python3-pip
       ```
     - **Arch Linux**:
       ```
       sudo pacman -S python python-pip
       ```
2. **Install Required Packages**:
   - In a terminal, run:
     ```
     pip3 install discord.py google-generativeai
     ```
3. **Create a Project Folder**:
   - Create a directory and navigate to it:
     ```
     mkdir DiscordAIBot && cd DiscordAIBot
     ```
   - Save the provided `discord_ai_bot.py` code as `discord_ai_bot.py` in this directory.

## Step 3: Configure Environment Variables

The `discord_ai_bot.py` code uses environment variables for security. Set them as follows:

### On Windows
1. Open Command Prompt and set the environment variables:
   ```
   setx GEMINI_API_KEY "your_gemini_api_key_here"
   setx DISCORD_BOT_TOKEN "your_discord_bot_token_here"
   ```
   Replace `your_gemini_api_key_here` and `your_discord_bot_token_here` with your actual keys.
2. Close and reopen Command Prompt to apply the changes.

### On Linux
1. Open a terminal and set the environment variables:
   ```
   export GEMINI_API_KEY="your_gemini_api_key_here"
   export DISCORD_BOT_TOKEN="your_discord_bot_token_here"
   ```
   Replace `your_gemini_api_key_here` and `your_discord_bot_token_here` with your actual keys.
2. To make these persistent, add them to your shell configuration file (e.g., `~/.bashrc` or `~/.zshrc`):
   ```
   echo 'export GEMINI_API_KEY="your_gemini_api_key_here"' >> ~/.bashrc
   echo 'export DISCORD_BOT_TOKEN="your_discord_bot_token_here"' >> ~/.bashrc
   source ~/.bashrc
   ```

## Step 4: Customize the Bot (Optional)
The bot will now prompt you for its name and a system instruction when you run the script.

### On Windows

1.  Open Command Prompt and navigate to your project folder:
    ```
    cd path\to\DiscordAIBot
    ```
2.  Run the bot:
    ```
    python discord_ai_bot.py
    ```
3.  The script will ask you to enter a name for your AI and a system instruction to define its personality. Enter your desired values. If you leave the system instruction blank, the bot will use a default persona.
4.  If successful, the console will display:
    ```
    Logged on as YourBotName#1234
    ```

### On Linux

1.  Open a terminal and navigate to your project folder:
    ```
    cd ~/DiscordAIBot
    ```
2.  Run the bot:
    ```
    python3 discord_ai_bot.py
    ```
3.  The script will ask you to enter a name for your AI and a system instruction to define its personality. Enter your desired values. If you leave the system instruction blank, the bot will use a default persona.
4.  If successful, the console will display:
    ```
    Logged on as YourBotName#1234
    ```

## Step 5: Run the Bot

### On Windows
1. Open Command Prompt and navigate to your project folder:
   ```
   cd path\to\DiscordAIBot
   ```
   Replace `path\to\DiscordAIBot` with the actual path.
2. Run the bot:
   ```
   python discord_ai_bot.py
   ```
3. If successful, you’ll see:
   ```
   Logged on as YourBotName#1234
   ```

### On Linux
1. Open a terminal and navigate to your project folder:
   ```
   cd ~/DiscordAIBot
   ```
2. Run the bot:
   ```
   python3 discord_ai_bot.py
   ```
3. If successful, you’ll see:
   ```
   Logged on as YourBotName#1234
   ```

## Step 6: Test the Vibes

1. Go to your Discord server where the bot is added.
2. Send a message using the trigger word or mention the bot (e.g., `Morpheous Hello!` or `@YourBotName What's up?`).
3. The bot should respond with AI-generated text based on the Gemini model.

## Troubleshooting

- **Bot Not Responding**:
  - Ensure the bot is online in your Discord server’s member list.
  - Verify it has `Send Messages` and `Read Messages/View Channels` permissions in the channel.
  - Check that the trigger word or mention matches the code exactly.
  - Confirm that both API keys are correctly set in environment variables.
- **"Module Not Found" Error**:
  - Reinstall the required libraries:
    ```
    pip install -U discord.py google-generativeai
    ```
    or
    ```
    pip3 install -U discord.py google-generativeai
    ```
  - Verify installation with:
    ```
    pip show discord.py google-generativeai
    ```
- **Connection Issues**:
  - Ensure a stable internet connection.
  - Check for outages in Discord or Google Cloud services.

## Pro Tips

- **Secure Your Keys**: Never share your Discord bot token or Gemini API key. Avoid hardcoding them in the script; use environment variables as shown.
- **Persistent Running**: Consider using a process manager like `pm2` (Linux) or running the bot in a screen session (`screen` on Linux) to keep it active.
- **Stop the Bot**: Press `Ctrl+C` in the terminal or Command Prompt to stop the bot.

## Thanks You, Legends!

Big shoutout to the folks who helped make this bot better:

- **darkhadesXIV**: Nailed it by switching to environment variables for securing API keys and keeping the code tight with the latest Discord API.
- **caliburn1337**: Dropped some awesome feedback that made this guide and setup way smoother.

# Guide to Setting Up a Discord AI Bot on Windows and Linux

This guide will walk you through setting up a Discord bot that chats using Google's Gemini AI. It works on Windows or Linux without any major hassles.

## What You Need

* A Discord account and a server where you have permission to add bots.
* A Google Cloud account to obtain a Gemini API key.
* Python 3.8 or newer installed on your system.
* A text editor of your choice (e.g., VS Code, Notepad++, Sublime Text).

## Step 1: Snag Your API Keys

### Discord Bot Token

1.  Go to the [Discord Developer Portal](https://discord.com/developers/applications).
2.  Create a new application.
3.  Navigate to the "Bot" tab in your application's settings.
4.  Click "Add Bot."
5.  Copy the **bot token**. Keep this safe!
6.  To add the bot to your server:
    * Go to "OAuth2" -> "URL Generator."
    * Select the `bot` scope.
    * Choose necessary permissions like `Send Messages` and `Read Messages/View Channels`.
    * Copy the generated URL and open it in your browser to invite the bot to your server.

### Google Gemini API Key

1.  Go to the [Google Cloud Console](https://console.cloud.google.com/).
2.  Create a new project if you don't have one.
3.  Enable the "Generative AI API" for your project.
4.  Create an API key. You can usually find this under "APIs & Services" -> "Credentials."
5.  Copy the generated **API key**. Keep this secure!

## Step 2: Set Up Your Environment

### On Windows

1.  **Get Python:**
    * Download the latest Python 3.x version from [python.org](https://www.python.org/downloads/).
    * Run the installer and **make sure to check the box that says "Add Python to PATH"** during installation.
    * Open Command Prompt and type `python --version` to verify the installation. You should see the Python version.
2.  **Install the Necessary Packages:**
    * Open Command Prompt.
    * Run the following command to install the required libraries:
        ```bash
        pip install discord.py google-generativeai
        ```
3.  **Create a Project Folder:**
    * Create a new folder on your computer (e.g., `DiscordAIBot`).
    * Save the Python bot code (explained in the next step) as `bot.py` inside this folder.

### On Linux

1.  **Check for Python:**
    * Most Linux distributions come with Python pre-installed. Open a terminal and check the version:
        ```bash
        python3 --version
        ```
    * If Python 3 is not installed, use your distribution's package manager:
        * **Ubuntu/Debian:**
            ```bash
            sudo apt update && sudo apt install python3 python3-pip
            ```
        * **Fedora:**
            ```bash
            sudo dnf install python3 python3-pip
            ```
        * **Arch Linux:**
            ```bash
            sudo pacman -S python python-pip
            ```
2.  **Install the Necessary Packages:**
    * Open a terminal and run:
        ```bash
        pip3 install discord.py google-generativeai
        ```
3.  **Create a Project Folder:**
    * Create a new directory for your bot and navigate into it:
        ```bash
        mkdir DiscordAIBot && cd DiscordAIBot
        ```
    * Save the Python bot code (explained in the next step) as `bot.py` inside this directory.

## Step 3: Tweak the Code

1.  Open the `discord_bot_ai.py` file in your text editor.
2.  Replace `ENTER_GOOGLE_API_KEY_HERE` with the Google Gemini API key you obtained.
3.  Replace `ENTER_DISCORD_KEY_HERE` with your Discord bot token.
4.  **(Optional) Customize the Bot's Persona:**
    * Uncomment the `model` section that includes `system_instruction`.
    * Modify the `system_instruction` to give your bot a specific personality. For example:
        ```python
        model = genai.GenerativeModel(model_name="gemini-pro", generation_config=generation_config)
        response = model.generate_content(
            [system_instruction, prompt]
        )
        ```
        Change `system_instruction` to something like: `"Act as a chill surfer dude named Wavey."`
5.  **(Optional) Change the Trigger Word:**
    * Look for the `on_message` event handler in the code.
    * Find the line that checks if the message content starts with the trigger word (e.g., `message.content.startswith('Morpheous ')`).
    * Change `'Morpheous '` to your desired trigger word, like `'!chat '`.

## Step 4: Fire Up the Bot

### On Windows

1.  Open Command Prompt.
2.  Navigate to your project folder:
    ```bash
    cd path\to\DiscordAIBot
    ```
    (Replace `path\to\DiscordAIBot` with the actual path to your folder).
3.  Run the bot script:
    ```bash
    python bot.py
    ```
4.  If everything is set up correctly, you should see a message like `Logged on as YourBotName#1234` in the Command Prompt.

### On Linux

1.  Open a terminal.
2.  Navigate to your project folder:
    ```bash
    cd ~/DiscordAIBot
    ```
3.  Run the bot script:
    ```bash
    python3 bot.py
    ```
4.  You should see a similar "Logged on as..." message in the terminal if the bot starts successfully.

## Step 5: Test the Vibes

1.  Go to your Discord server where you added the bot.
2.  Send a message starting with your trigger word followed by your query (e.g., `Morpheous Yo, what's good?` or `!chat What's the weather like?`).
3.  The bot should respond with AI-generated text.

## If It's Acting Up

* **Bot isn't responding?**
    * Check if the bot is online in your Discord server's member list.
    * Verify that the bot has the necessary permissions (Send Messages, Read Messages/View Channels) in the channel you're trying to chat in.
    * Ensure that the trigger word in your message exactly matches the one in your `bot.py` code.
    * Double-check that your API keys (both Discord and Google) are correct and haven't expired or been revoked.
* **"Module not found" error?**
    * This usually means the required Python libraries (`discord.py` and `google-generativeai`) are not installed correctly.
    * Try reinstalling them using pip:
        ```bash
        pip install -U discord.py google-generativeai
        ```
        or
        ```bash
        pip3 install -U discord.py google-generativeai
        ```
    * You can also check if they are installed by running `pip show discord.py` or `pip3 show google-generativeai`.
* **Connection issues?**
    * Make sure your internet connection is stable.
    * Check if the Discord API or Google Cloud services are experiencing any outages.

## Pro Tips

* **Secure Your Keys:** Never share your Discord bot token or Google Gemini API key with anyone. Treat them like passwords.
* **Internet Connection:** The bot needs an active internet connection to communicate with Discord and Google's AI services.
* **Stopping the Bot:** To stop the bot, go to the terminal or Command Prompt where it's running and press `Ctrl+C`.

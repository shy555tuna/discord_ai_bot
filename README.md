Guide to Implement Discord AI Bot on Windows and Linux
This guide explains how to set up and run the provided Discord AI bot code, which uses the Discord API and Google's Generative AI (Gemini) on Windows and Linux.
Prerequisites

A Discord account and a server where you have permission to add bots.
A Google Cloud account with access to the Gemini API.
Python 3.8 or higher installed.
A text editor (e.g., VS Code, Notepad++, or any IDE).

Step 1: Obtain API Keys

Discord Bot Token:
Go to the Discord Developer Portal.
Create a new application, then add a bot under the "Bot" tab.
Copy the bot token.
Invite the bot to your server:
Under "OAuth2 > URL Generator," select bot scope and permissions like Send Messages and Read Messages/View Channels.
Use the generated URL to add the bot to your server.




Google Gemini API Key:
Go to Google Cloud Console.
Create a project, enable the Generative AI API, and generate an API key.
Copy the API key.



Step 2: Set Up the Environment
On Windows

Install Python:
Download Python from python.org.
Run the installer, ensuring you check "Add Python to PATH."
Verify installation: Open Command Prompt and run python --version.


Install Dependencies:
Open Command Prompt.
Install required Python packages:pip install discord.py google-generativeai




Create Project Folder:
Create a folder (e.g., DiscordAIBot).
Save the provided code as bot.py in this folder.



On Linux

Install Python:
Most Linux distributions come with Python pre-installed. Verify with:python3 --version


If not installed, use your package manager:
Ubuntu/Debian: sudo apt update && sudo apt install python3 python3-pip
Fedora: sudo dnf install python3 python3-pip
Arch: sudo pacman -S python python-pip




Install Dependencies:
Open a terminal and install required packages:pip3 install discord.py google-generativeai




Create Project Folder:
Create a folder (e.g., mkdir DiscordAIBot && cd DiscordAIBot).
Save the provided code as bot.py in this folder.



Step 3: Configure the Code

Open bot.py in a text editor.
Replace ENTER_GOOGLE_API_KEY_HERE with your Google Gemini API key.
Replace ENTER_DISCORD_KEY_HERE with your Discord bot token.
(Optional) Customize the AI persona:
Uncomment the model section with system_instruction.
Modify the system_instruction to define the bot’s personality (e.g., "Act as a friendly pirate named Captain Chat").


(Optional) Change the command prefix:
Modify Morpheous in the on_message function to your preferred prefix (e.g., !chat).



Step 4: Run the Bot
On Windows

Open Command Prompt and navigate to your project folder:cd path\to\DiscordAIBot


Run the bot:python bot.py


If successful, you’ll see Logged on as <BotName>.

On Linux

Open a terminal and navigate to your project folder:cd ~/DiscordAIBot


Run the bot:python3 bot.py


If successful, you’ll see Logged on as <BotName>.

Step 5: Test the Bot

Go to your Discord server.
Send a message starting with the prefix (e.g., Morpheous Hello, how are you?).
The bot should respond with an AI-generated message.

Troubleshooting

Bot not responding:
Ensure the bot is online and has proper permissions in the server.
Check that the prefix matches the one in the code.
Verify API keys are correct and not expired.


Module not found:
Confirm discord.py and google-generativeai are installed.
Use pip show discord.py or pip3 show google-generativeai to verify.


Connection errors:
Check your internet connection.
Ensure API services (Discord and Google) are operational.



Notes

Keep your API keys and bot token secure; do not share them publicly.
The bot requires an active internet connection to communicate with Discord and Google’s API.
To stop the bot, press Ctrl+C in the terminal/command prompt.
Tweak however you like! Enjoy and have fun~

from constants import Client
from bot import Bot
from utils.extensions import walk_extensions

# Bot Instance
bot = Bot()

# Loading all the Cogs/Extensions
for ext in walk_extensions():
    bot.load_extension(ext)

# Start the Bot
bot.run(Client.token)

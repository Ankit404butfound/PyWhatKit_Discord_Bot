from google.cloud import bigquery
import os
import discord
from discord.ext import commands

token = "ODMwNjUzMzkyOTM3NTQ5ODQ0.YHJ0QQ.gNUV1VRjm4Fau7WAVshKtvvhyRc"
bot = commands.Bot(command_prefix = "")


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "config.json"
client = bigquery.Client()

query = """
   SELECT count(*) as Downloads
FROM `bigquery-public-data.pypi.file_downloads`
WHERE file.project = 'pywhatkit'
  -- Only query the last 30 days of history
  AND DATE(timestamp)
    BETWEEN DATE_SUB(CURRENT_DATE(), INTERVAL 0 DAY)
    AND CURRENT_DATE()
"""


@bot.event
async def on_ready():
    print('Bot is ready')


@bot.event
async def on_message(message):
    print(message.content)
    if message.author == bot.user:
        return

    if message.content == ".test":
        await message.channel.send("Bot is working")

    if message.content == ".download_count":
        query_job = client.query(query)  # Make an API request.
        print("The query data:")
        row = [*query_job][0]
        print(row[0])
        await message.channel.send("Pywhatkit has been downloaded %s times in time range between 00:00 UTC till now."%str(row[0]))

bot.run(token)

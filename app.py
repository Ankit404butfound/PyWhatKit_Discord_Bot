from google.cloud import bigquery
import os
import discord
from discord.ext import commands
import asyncio

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

query_1 = """
   SELECT count(*) as Downloads
FROM `bigquery-public-data.pypi.file_downloads`
WHERE file.project = 'pywhatkit'
  -- Only query the last 30 days of history
  AND DATE(timestamp)
    BETWEEN DATE_SUB(CURRENT_DATE(), INTERVAL 1 DAY)
    AND CURRENT_DATE()
"""


@bot.event
async def on_ready():
    print('Bot is ready')
    asyncio.gather(send_count())


async def send_count():
    while True:
        channel = bot.get_channel(839422789849317406)
        query_job = client.query(query_1)
        await channel.send("Pywhatkit has been downloaded %s times in last 24 hours."%str([*query_job][0][0]))
        await asyncio.sleep(10)


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

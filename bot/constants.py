import os
import discord
from discord.ext import commands
from google.cloud import bigquery

token = os.environ["TOKEN"]
intents = discord.Intents.all()
intents.members = True

bot = discord.Client(intents=intents)


file = open("config.json","w")
file.write(os.environ.get("CONFIG_JSON"))
file.close()


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

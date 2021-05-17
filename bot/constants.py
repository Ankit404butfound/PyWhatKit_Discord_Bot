import os
import discord
from discord.ext import commands
from google.cloud import bigquery
import psycopg2


token = os.environ["TOKEN"]
intents = discord.Intents.all()
intents.members = True

bot = discord.Client(intents=intents)


file = open("config.json","w")
file.write(os.environ.get("CONFIG_JSON"))
file.close()


allowed_roles = ["Contributors"]
drunk_list = ['Yes','No','Maybe','Nah','Yea','Are you serious','I dont want to hear this','What! LoL',
                           'Am i dumb','bluh bluh','Are you mad','God!','Am i drunk','Are you drunk','I doubt','Smells nothing',
                           'Who cares','Its mean','Cool but no','Is it true','Its hard','Going to sereach','Felt dumb','Oh! no',
                           'blah blah','let my soul on rest']
    
sad_words = ["sad", "depressed", "unhappy", "angry","miserable","die","kill","crying","waste","not working"]

starter_encouragements = [  "Cheer up!",  "Hang in there.",  "You are a great person / bot!", "Don’t give up","Keep pushing",
                                "Keep fighting!","Stay strong Never give up" "Never say!", "Come on! You can do it!","Believe in yourself"]


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "config.json"
client = bigquery.Client()

conn = psycopg2.connect(os.environ.get("DATABASE_URL"))
cur = conn.cursor()

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

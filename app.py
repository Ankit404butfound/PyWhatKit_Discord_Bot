from google.cloud import bigquery
import os
import discord
from discord.ext import commands
import asyncio

token = os.environ["TOKEN"]
intents = discord.Intents.all()
#intents.members = True

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


def execute(code):
    #code = code.replace("\n","\\n").replace("\t","\\t").replace("\r","\\r")
    file = open("agent.py","w",encoding="utf-8")
    file.write(code)
    file.close()
    os.system("python executor.py > output.txt")
    data = open("output.txt",encoding="utf-8").read()
    if data != "":
        return data if len(data) <= 4090 else "Output too big, returning first 4000 characters\n"+data[:4000]
    else:
        return "No output statement provided"


@bot.event
async def on_member_join(member):
    await member.guild.system_channel.send(f"""Hello {member.mention} and Thanks for joining PyWhatKit's server.
Be sure to follow the <#830332694231384074> of this server.
Please head over to <#830319507360186389> and consider introducing yourself.""")
   
   
@bot.event
async def on_ready():
    print('Bot is ready')
    asyncio.gather(send_count())


async def send_count():
    while True:
        channel = bot.get_channel(839422789849317406)
        query_job = client.query(query_1)
        await channel.send("Pywhatkit has been downloaded %s times in last 24 hours."%str([*query_job][0][0]))
        await asyncio.sleep(86400)


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
    
    if ".execute" in message.content:
        mod = False
        roles = message.author.roles
        for role in roles:
           if role.name == 'Mod Level 1':
               mod = True
        
        if not mod:
           if "import" in message.content or "exce" in message.content or "eval" in message.content:
              await message.channel.send("`ERROR: You have limited access to this bot`")
              return
        code = message.content.replace(".execute ","")
        await message.channel.send("`"+execute(code)+"`")
         

bot.run(token)

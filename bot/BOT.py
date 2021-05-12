import asyncio
import discord
from discord.ext import commands
from constants import *
from download_notifier import send_count
from code_executor import execute
from my_psql import execute_sql, fetch_todo, add_todo, todo_done

import asyncio

class Bot:
    def __init__(self):
        self.client = client
        self.bot = bot
        


    def download_notifier():
        send_count()
        

    @bot.event
    async def on_member_join(member):
        await member.guild.system_channel.send(f"""Hello {member.mention} and Thanks for joining PyWhatKit's server.
Be sure to follow the <#830332694231384074> of this server.
Please head over to <#830319507360186389> and consider introducing yourself.""")
       
       
    @bot.event
    async def on_ready():
        print('Bot is ready')
        asyncio.gather(send_count())


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

        if ".pgrsql" in message.content:
            sql = message.content.replace(".pgrsql ","")
            roles = message.author.roles
            for role in roles:
               if role.name in allowed_roles:
                   mod = True
            if mod:
                await message.channel.send("`"+execute_sql(sql)+"`")
            else:
                await message.channel.send("`ERROR: You have limited access to this bot`")

        if "#add_todo" in message.content:
            roles = message.author.roles
            task = message.content.replace("#add_todo ","")
            for role in roles:
               if role.name in allowed_roles:
                   mod = True
            if mod:
                await message.channel.send(f"`{add_todo(message.author.id, task)}`")

        if "#what_todo" in message.content:
            roles = message.author.roles
            for role in roles:
               if role.name in allowed_roles:
                   mod = True

            if mod:
                tasks = ""
                dbs = fetch_todo(message.author.id)
                for task in dbs:
                    tasks = f"{tasks}Task_id_{task[0]}. {task[1]}\n"
                    
                if tasks != "":
                    await message.channel.send(f"`Here's the list of your pending tasks\n{tasks}`")
                else:
                    await message.channel.send(f"`You have no pending tasks`")

        if "#todo_done" in message.content:
            roles = message.author.roles
            task_id = message.content.replace("#todo_done ","")
            for role in roles:
               if role.name in allowed_roles:
                   mod = True
            if mod:
                if todo_done(task_id):
                    await message.channel.send(f"`Done`")
                else:
                    await message.channel.send(f"`Task ID not found`")
            
    def start(self):
        self.bot.run(token)

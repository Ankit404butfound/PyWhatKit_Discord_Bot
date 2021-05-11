from google.cloud import bigquery
import asyncio
from constants import *

async def send_count():
    while True:
        channel = bot.get_channel(839422789849317406)
        query_job = client.query(query_1)
        await channel.send("Pywhatkit has been downloaded %s times in last 24 hours."%str([*query_job][0][0]))
        await asyncio.sleep(86400)

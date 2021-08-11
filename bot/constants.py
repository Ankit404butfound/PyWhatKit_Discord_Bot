try:
    from dotenv import load_dotenv

    print("Found a .env file, loading environment variables from it!")
    load_dotenv()
except ModuleNotFoundError:
    pass

import os
from typing import NamedTuple

__all__ = ["Channels", "Client", "Roles"]


class Channels(NamedTuple):
    """ID's for the channels"""

    welcome = 863847136403914796
    introduce = 863847136403914797
    rules = 863847136403914798
    announcements = 866324696970690561


class Client(NamedTuple):
    """Details for the Bot"""

    name = "PyWhatKit"
    guild = int(os.environ.get("GUILD_ID", 863847136076103710))
    prefix = os.environ.get("PREFIX", "!")
    token = os.environ.get("BOT_TOKEN")
    bot_repo = "https://github.com/Ankit404butfound/PyWhatKit_Discord_Bot"
    wiki = "https://github.com/Ankit404butfound/PyWhatKit/wiki"
    module_repo = "https://github.com/Ankit404butfound/PyWhatKit"


class Roles(NamedTuple):
    """Role ID's"""

    admin = 863847136076103716
    owner = 863847136076103717
    mod_2 = 863847136076103715
    mod_1 = 863847136076103714
    helper = 863847136076103713
    contributors = 863847136076103712
    announcements = 866321812199440444
    banned = 866614754416001074
    video = 874344502658203668

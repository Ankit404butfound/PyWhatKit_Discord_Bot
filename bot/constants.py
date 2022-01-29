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

    welcome = 830319475387531296
    introduce = 830319507360186389
    rules = 830332694231384074
    announcements = 830319507360186389  # 830340707951968267


class Client(NamedTuple):
    """Details for the Bot"""

    name = "PyWhatKit"
    guild = int(os.environ.get("GUILD_ID", 830315801629949954))
    prefix = os.environ.get("PREFIX", "!")
    token = os.environ.get("TOKEN")
    bot_repo = "https://github.com/Ankit404butfound/PyWhatKit_Discord_Bot"
    wiki = "https://github.com/Ankit404butfound/PyWhatKit/wiki"
    module_repo = "https://github.com/Ankit404butfound/PyWhatKit"


class Roles(NamedTuple):
    """Role ID's"""

    announcements = 866624699432435712
    banned = 866624846087979049
    video = 866628190604623902

import discord
from discord.ext import commands

import constants

__all__ = ["Bot"]


class Bot(commands.Bot):
    """
    Base bot Instance.

    A subclass of commands.Bot
    """

    def __init__(self) -> None:
        super().__init__(command_prefix=constants.Client.prefix,
                         description="Online", intents=discord.Intents.all())

    async def on_ready(self) -> None:
        """Using self.wait_until_ready() to wait for the Guild to be Available"""

        await self.wait_until_ready()
        await Bot.change_presence(self, activity=discord.Game(name="!help"))
        print(f"Logged on as {self.user}")

    async def on_member_join(self, member: discord.Member) -> None:
        """Welcome message when a New Member Joins"""

        await self.get_channel(constants.Channels.welcome).send(
            f"Welcome to the PyWhatKit Discord Server, {member.mention}.\n"
            f"Please take some time to read through the server <#{constants.Channels.rules}>.\n"
            f"Finally please be kind to everyone and enjoy your time here.")

    def add_cog(self, cog: commands.Cog) -> None:
        """Adds a Cog"""

        super().add_cog(cog)

    def add_command(self, command: commands.Command) -> None:
        """Adds a command"""

        super().add_command(command)

    def remove_cog(self, name: str) -> None:
        """Removes a Cog"""

        super().remove_cog(name)

    def remove_command(self, name: str) -> None:
        """Removes a Command"""

        super().remove_command(name)

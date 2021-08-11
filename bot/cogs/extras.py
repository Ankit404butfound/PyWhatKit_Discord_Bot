import discord
from discord.ext import commands

from bot import constants
from utils.roles import check_self_role


class Extras(commands.Cog):
    """
    Extra Commands
    """

    def __init__(self, bot: commands.Bot) -> None:
        super().__init__()
        self.bot = bot

    @commands.command(name="ping")
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def ping(self, ctx: commands.Context) -> None:
        """
        Sends a Message with the Latency of the Bot
        """

        await ctx.send(f"Pong: {round(self.bot.latency * 1000)} ms 🚀")

    @commands.command(name="subscribe")
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def subscribe(self, ctx: commands.Context) -> None:
        """
        Subscribe to Announcements
        """

        has_role = check_self_role(ctx, constants.Roles.announcements)

        if has_role:
            await ctx.send(f"{ctx.author.mention} You're already Subscribed!")
            return

        await ctx.author.add_roles(discord.Object(constants.Roles.announcements), reason="Subscribed to announcements")

        await ctx.send(f"{ctx.author.mention} Subscribed to <#{constants.Channels.announcements}>")

    @commands.command(name="unsubscribe")
    @commands.command(1, 15, commands.BucketType.user)
    async def unsubscribe(self, ctx: commands.Context) -> None:
        """
        Unsubscribe to Announcements
        """

        has_role = check_self_role(ctx, constants.Roles.announcements)

        if has_role:
            await ctx.author.remove_roles(discord.Object(constants.Roles.announcements), reason="Unsubscribe to "
                                                                                                "announcements")
            await ctx.send(f"{ctx.author.mention} Unsubscribed to <#{constants.Channels.announcements}>")
            return

        await ctx.send(f"{ctx.author.mention} You're not Subscribed to <#{constants.Channels.announcements}>")

    @commands.command(name="prefix")
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def prefix(self, ctx: commands.Context) -> None:
        """
        Get the Bot Prefix
        """

        await ctx.send(f"{ctx.author.mention} the Bot Prefix is {self.bot.command_prefix}")


def setup(bot: commands.Bot) -> None:
    bot.add_cog(Extras(bot))

from typing import Optional

import discord
from discord.ext import commands

import utils.db_parser as db_parser
from bot import constants


class Docs(commands.Cog):
    """
    Provides Docs and Examples
    """

    def __init__(self, bot: commands.Bot) -> None:
        super().__init__()
        self.bot = bot

    @commands.command(name="link")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def link(self, ctx: commands.Context, name: str) -> None:
        """
        Important Links
        """

        if name.lower() == "wiki":
            await ctx.send(constants.Client.wiki)
        elif name.lower() == "module":
            await ctx.send(constants.Client.module_repo)
        elif name.lower() == "bot":
            await ctx.send(constants.Client.bot_repo)
        else:
            await ctx.send("Please enter either wiki, bot or module!")

    @commands.command(name="docs")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def docs(self, ctx: commands.Context, *args: Optional[str]) -> None:
        """
        Search the Docs for a particular Function
        """

        data = db_parser.search_for_docs(" ".join(args))
        if not data:
            return await ctx.send(f"{ctx.author.mention} No Results Found!")

        topic, descp, argums, returs, link = data
        embed = discord.Embed(title=topic, color=discord.Color.random())
        embed.add_field(name="Description",
                        value=f"```\n{descp}```", inline=False)
        embed.add_field(name="Arguments",
                        value=f"```python\n{argums}```", inline=False)
        embed.add_field(
            name="Returns", value=f"```python\n{returs}```", inline=False)
        embed.add_field(name="Link", value=link, inline=False)
        await ctx.send(ctx.author.mention, embed=embed)

    @commands.command(name="example")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def examples(self, ctx: commands.Context, *args: Optional[str]) -> None:
        """
        Examples for a Function
        """
        data = db_parser.search_for_example(" ".join(args))

        if not data[0]:
            return await ctx.send(f"{ctx.author.mention} No Results Found!")

        embed = discord.Embed(title=data[0], color=discord.Color.random())
        for info in data[1]:
            embed.add_field(
                name=info[1], value=f"```python\n{info[0]}```", inline=False)
        await ctx.send(ctx.author.mention, embed=embed)

    @commands.command(name="exception")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def exception(self, ctx: commands.Context, *args: Optional[str]) -> None:
        """
        Get Information about a particular Exception
        """

        data = db_parser.search_for_exception(" ".join(args))
        if not data:
            return await ctx.send(f"{ctx.author.mention} No Results Found!")

        embed = discord.Embed(title=data[0], color=discord.Color.random())
        embed.add_field(name="Description",
                        value=f"`{data[1]}`", inline=False)
        embed.add_field(name="Fix", value=f"`{data[2]}`", inline=False)
        await ctx.send(ctx.author.mention, embed=embed)

    @commands.command(name="list")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def list(self, ctx: commands.Context, topic: str) -> None:
        """
        List the Available Searches for the !docs and !exception Commands
        """

        if "function" in topic.lower():
            functions = "\n".join(f":rocket: {i[0]}" for i in db_parser.execute(
                "SELECT topic FROM command"))
            embed = discord.Embed(
                title="Available searches", description=functions, color=discord.Color.random())
            await ctx.send(ctx.author.mention, embed=embed)

        elif "exception" in topic.lower():
            exceptions = "\n".join(f":rocket: {i[0]}" for i in db_parser.execute(
                "SELECT topic FROM exception"))
            embed = discord.Embed(
                title="Available searches", description=exceptions, color=discord.Color.random())
            await ctx.send(ctx.author.mention, embed=embed)

        else:
            return await ctx.send(f"{ctx.author.mention} Please enter a Valid Value (function, exception)!")


def setup(bot: commands.Bot) -> None:
    bot.add_cog(Docs(bot))

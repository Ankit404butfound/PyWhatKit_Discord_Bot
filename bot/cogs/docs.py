from typing import Optional

from discord.ext import commands

from bot import constants


class Docs(commands.Cog):
    """
    Provides Docs and Examples
    """

    def __init__(self, bot: commands.Bot) -> None:
        super().__init__()
        self.bot = bot

    @commands.command(name="link")
    @commands.cooldown(1, 15, commands.BucketType.user)
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
            await ctx.send("Please enter either wiki, bot or module")

    # TODO: Re-Implement these Commands after Setting up the Database on Heroku
    # @commands.command(name="docs")
    # async def docs(self, ctx: commands.Context, *args: Optional[str]) -> None:
    #     """
    #     Search the Docs for a particular Function
    #     """
    #
    #     embed = parser.create_docs_embed(docs=parser.return_docs(' '.join(args), "commands"))
    #     await ctx.send(ctx.author.mention)
    #     await ctx.send(embed=embed)

    # @commands.command(name="example")
    # async def examples(self, ctx: commands.Context, *args: Optional[str]) -> None:
    #     """
    #     Examples for a Function
    #     """
    #
    #     embed = parser.examples_embed(docs=parser.return_docs(' '.join(args), "commands"))
    #     await ctx.send(embed=embed)

    # @commands.command(name="exception")
    # async def exception(self, ctx: commands.Context, *args: Optional[str]) -> None:
    #     """
    #     Get Information about a particular Exception
    #     """
    #
    #     embed = parser.exception_embed(docs=parser.return_docs(' '.join(args), "exception"))
    #     await ctx.send(embed=embed)

    # @commands.command(name="list")
    # async def list(self, ctx: commands.Context, topic: str) -> None:
    #     """
    #     List the Available Searches for the !docs and !exception Commands
    #     """
    #
    #     embed = parser.return_topics_embed(_type=topic)
    #     if embed is None:
    #         await ctx.send(f"{topic} is not a Valid Option, Choose from functions and exceptions")
    #         return

    #     await ctx.send(embed=embed)


def setup(bot: commands.Bot) -> None:
    bot.add_cog(Docs(bot))

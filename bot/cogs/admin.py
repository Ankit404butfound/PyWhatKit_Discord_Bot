import discord
from discord.ext import commands

import constants
from utils.roles import check_self_role, check_member_role
from utils.db_parser import execute


class ManageCogs(commands.Cog):
    """
    Manage Cogs and Commands
    """

    def __init__(self, bot: commands.Bot) -> None:
        super().__init__()
        self.bot = bot

    @commands.command(name="unload_cog")
    @commands.has_any_role("Mod Level 2")
    async def unload_cog(self, ctx: commands.Context, name: str) -> None:
        """
        Unload a Cog
        """

        self.bot.remove_cog(name)
        await ctx.send(f"Cog {name} has been Unloaded!")

    # FIXME: Loading doesn't Work
    # @commands.command(name="load_cog")
    # @commands.has_any_role("Mod Level 2")
    # async def load_cog(self, ctx: commands.Context, name: str) -> None:
    #     """
    #     Load a Cog
    #     """
    #
    #     self.bot.add_cog(commands.Cog(f"bot.cogs.{name}"))
    #     await ctx.send(f"Cog {name} has been Loaded!")

    @commands.command(name="remove_command")
    @commands.has_any_role("Mod Level 2")
    async def remove_command(self, ctx: commands.Context, name: str) -> None:
        """
        Removes a Command
        """

        self.bot.remove_command(name)
        await ctx.send(f"Command {name} has been Removed!")

    # FIXME: Adding Command doesn't Work
    # @commands.command(name="add_command")
    # @commands.has_any_role("Mod Level 2")
    # async def add_command(self, ctx: commands.Context, name: commands.Command) -> None:
    #     """
    #     Adds a Command
    #     """
    #
    #     self.bot.add_command(name)
    #     await ctx.send(f"Command {name} has been Added!")


class Moderation(commands.Cog):
    """
    Commands for Server Moderation
    """

    def __init__(self, bot: commands.Bot) -> None:
        super().__init__()
        self.bot = bot

    @commands.command(name="ban")
    @commands.has_any_role("Mod Level 2")
    async def ban(self, ctx: commands.Context, member: discord.Member, *reason: str) -> None:
        """
        Permanently Ban a Member
        """

        reason = [x for x in reason]
        await member.ban(reason=' '.join(reason))
        await ctx.message.delete()
        await ctx.send(embed=discord.Embed(title=f"Banned {member.display_name}",
                                           description=f"Banned by {ctx.author} for {' '.join(reason)}",
                                           colour=discord.Color.random()))

    @commands.command(name="unban")
    @commands.has_any_role("Mod Level 2")
    async def unban(self, ctx: commands.Context, id: int) -> None:
        """
        Remove the Permanent Ban
        """

        user = await self.bot.fetch_user(id)
        await ctx.guild.unban(user)
        await ctx.message.delete()
        await ctx.send(embed=discord.Embed(title=f"Unban {user.display_name}",
                                           description=f"{ctx.author} has removed the Ban",
                                           colour=discord.Color.random()))

    # TODO: Improve the Message Format
    @commands.command(name="listbans")
    @commands.has_any_role("Mod Level 1")
    async def list_bans(self, ctx: commands.Context) -> None:
        """
        Sends a Message with the User ID and the Name of Banned Users
        """

        bans = await ctx.guild.bans()

        banned = [str(x) for x in bans]

        if banned:
            await ctx.send(embed=discord.Embed(title="Banned Users",
                                               description=" ".join(banned),
                                               colour=discord.Color.random()))
        else:
            await ctx.send(embed=discord.Embed(title="Banned Users",
                                               description="No Banned Users",
                                               colour=discord.Color.random()))

    @commands.command(name="warn")
    @commands.has_any_role("Mod Level 1")
    async def warn(self, ctx: commands.Context, member: discord.Member, *reason: str) -> None:
        """
        Warn a Member for Violation of Rules
        """

        member_id = member.id
        num_of_warns = execute(
            f"SELECT num_of_warnings FROM flagged_user WHERE user_id={member_id}")
        num_of_warns = 0 if not num_of_warns else num_of_warns[0][0]
        message = [x for x in reason]

        if num_of_warns < 2:
            warn_message = f"Warning for {member.display_name}"

        elif num_of_warns == 2:
            warn_message = f"Last warning for {member.display_name}"

        elif num_of_warns >= 3:
            await member.ban(reason=' '.join(message))
            await ctx.send(embed=discord.Embed(title=f"{member.display_name} has been banned",
                                               description=f"Warned multiple times by {ctx.author} for {' '.join(message) if message else 'unknown reason'}",
                                               colour=discord.Color.random()))
            execute(f"DELETE FROM flagged_user WHERE user_id={member_id}", "w")
            return

        if message:
            await ctx.send(embed=discord.Embed(title=warn_message,
                                               description=f"Warned by {ctx.author} for {' '.join(message)}",
                                               colour=discord.Color.random()))
        else:
            await ctx.send(embed=discord.Embed(title=warn_message,
                                               description=f"Warned by {ctx.author}",
                                               colour=discord.Color.random()))

        if num_of_warns == 0:
            if execute(f"INSERT INTO flagged_user VALUES ({member_id}, 1)", "w"):
                print("INSERTED")
        else:
            execute(
                f"UPDATE flagged_user SET num_of_warnings={num_of_warns+1} WHERE user_id={member_id}", "w")

    @commands.command(name="clear")
    @commands.has_any_role("Mod Level 1")
    async def clear(self, ctx: commands.Context, amount: int = 2) -> None:
        """
        Clear a particular Amount of Messages
        """

        await ctx.channel.purge(limit=amount)
        await ctx.send(f"{ctx.author} deleted {amount} Messages")

    @commands.command(name="kick")
    @commands.has_any_role("Mod Level 1")
    async def kick(self, ctx: commands.Context, member: discord.Member, *reason: str) -> None:
        """
        Remove a Member
        """

        await member.kick(reason=" ".join(reason))
        await ctx.message.delete()
        reason = [x for x in reason]
        await ctx.send(embed=discord.Embed(title=f"Kicked {member.display_name}",
                                           description=f"Kicked by {ctx.author} for {' '.join(reason)}" if reason else f"Kicked by {ctx.author}",
                                           colour=discord.Color.random()))

    @commands.command(name="tempban")
    @commands.has_any_role("Mod Level 1")
    async def tempban(self, ctx: commands.Context, member: discord.Member, *reason: str) -> None:
        """
        Temporarily Ban a Member
        """

        has_role = check_self_role(ctx, constants.Roles.banned)
        await ctx.message.delete()
        if has_role:
            await ctx.send(f"{member.mention} is already under Temporary Ban!")
            return

        reason = [x for x in reason]
        await member.add_roles(discord.Object(constants.Roles.banned), reason=' '.join(reason))

        await ctx.send(embed=discord.Embed(title="Temporary Ban",
                                           description=f"{ctx.author} has applied Temporary Ban to {member.mention} for {' '.join(reason)}",
                                           colour=discord.Color.random()))

    @commands.command(name="removetempban")
    @commands.has_any_role("Mod Level 1")
    async def remove_temp_ban(self, ctx: commands.Context, member: discord.Member) -> None:
        """
        Remove the Temporary Ban from a Member
        """

        has_role = check_member_role(member, constants.Roles.banned)
        await ctx.message.delete()
        if has_role:
            await member.remove_roles(discord.Object(constants.Roles.banned), reason="Temporary Ban Removed")

            await ctx.send(embed=discord.Embed(title="Temporary Ban Removed",
                                               description=f"{ctx.author} has removed the Temporary Ban from {member.mention}!",
                                               colour=discord.Color.random()))
            return

        await ctx.send(f"{member.mention} is not under Temporary Ban!")

    @commands.command(name="stream")
    @commands.has_any_role("Mod Level 1")
    async def stream(self, ctx: commands.Context, member: discord.Member, reason: str) -> None:
        """
        Give Streaming Permission
        """

        has_role = check_member_role(
            member=member, role_id=constants.Roles.video)
        if has_role:
            await ctx.send(f"{member.mention} already has Streaming Permission!")
            return

        await member.add_roles(discord.Object(constants.Roles.video), reason=reason)
        await ctx.send(f"{ctx.author.mention} gave Streaming Permission to {member.mention}")

    @commands.command(name="removestream")
    @commands.has_any_role("Mod Level 1")
    async def removestream(self, ctx: commands.Context, member: discord.Member) -> None:
        """
        Remove Streaming Permission
        """

        has_role = check_member_role(
            member=member, role_id=constants.Roles.video)
        if has_role:
            await member.remove_roles(discord.Object(constants.Roles.video), reason="Remove Streaming Permission")
            await ctx.send(f"{ctx.author.mention} has removed Streaming Permission from {member.mention}")
            return

        await ctx.send(f"{member.mention} doesn't have Streaming Permission")

    @commands.command(name="change_prefix")
    @commands.has_any_role("Mod Level 2")
    async def change_prefix(self, ctx: commands.Context, prefix: str) -> None:
        """
        Change the Bot Prefix
        """

        if prefix == self.bot.command_prefix:
            await ctx.send(f"{prefix} is the current Bot Prefix")
            return

        self.bot.command_prefix = prefix
        await self.bot.change_presence(activity=discord.Game(name=f"{prefix}help"))
        await ctx.send(f"{prefix} is the updated Bot Prefix")


def setup(bot: commands.Bot) -> None:
    bot.add_cog(ManageCogs(bot))
    bot.add_cog(Moderation(bot))

import discord
from discord.ext import commands


def check_self_role(ctx: commands.Context, role_id: int) -> bool:
    """
    Checks if the Author of the Context has the Role
    """

    return any(role.id == role_id for role in ctx.author.roles)


def check_member_role(member: discord.Member, role_id: int) -> bool:
    """
    Checks if the Member has the Role
    """

    return any(role.id == role_id for role in member.roles)

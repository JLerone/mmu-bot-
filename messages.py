from discord.ext import commands
import discord

def setup(bot: commands.Bot):
    warnings = {}

    @bot.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(ctx, amount: int):
        await ctx.channel.purge(limit=amount)
        await ctx.send(f"Deleted {amount} messages")

    @bot.command()
    @commands.has_permissions(kick_members=True)
    async def kick(ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f"Kicked {member} | Reason: {reason}")

    @bot.command()
    @commands.has_permissions(ban_members=True)
    async def ban(ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f"Banned {member} | Reason: {reason}")

    @bot.command()
    @commands.has_permissions(kick_members=True)
    async def warn(ctx, member: discord.Member, *, reason=None):
        user_id = str(member.id)

        if user_id not in warnings:
            warnings[user_id] = []

        warnings[user_id].append(reason or "No reason provided")

        await ctx.send(f"{member.mention} has been warned. Total warnings: {len(warnings[user_id])}")
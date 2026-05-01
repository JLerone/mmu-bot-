from discord.ext import commands
import discord

def setup(bot: commands.Bot):

    @bot.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(ctx, amount: int):
        await ctx.channel.purge(limit=amount)
        await ctx.send(f"Deleted {amount} messages")
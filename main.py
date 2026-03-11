import os
import discord
from discord.ext import commands

print("✅ БОТ НАЧАЛ ЗАПУСК")

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user} (id={bot.user.id})")

@bot.command()
async def ping(ctx: commands.Context):
    await ctx.send("works 🖐🏻")

def main():
    if not TOKEN:
        raise RuntimeError("❌ DISCORD_TOKEN не задан. В PowerShell: $env:DISCORD_TOKEN=\"...\"")
    bot.run(TOKEN)

if __name__ == "__main__":
    main()

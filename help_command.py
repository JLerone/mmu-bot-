def setup(bot: commands.Bot):

    @bot.command()
    async def helpme(ctx: commands.Context):
        help_text = """
Available commands:

!ping - Check if the bot is working
!helpme - Show this help message
"""
        await ctx.send(help_text)
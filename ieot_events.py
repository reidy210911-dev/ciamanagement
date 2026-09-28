import discord
from discord.ext import commands

class IEOTEvents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        @commands.command()
        async def ieot(self, ctx, event_name: str, event_date: str):
            await ctx.send(f'IEOT event {event_name} scheduled for {event_date}')

            async def setup(bot):
                await bot.add_cog(IEOTEvents(bot))

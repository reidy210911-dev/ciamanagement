import discord
from discord.ext import commands

class Operations(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        @commands.command()
        async def operation(self, ctx, operation_name: str, operation_date: str):
            await ctx.send(f'Operation {operation_name} scheduled for {operation_date}')

            async def setup(bot):
                await bot.add_cog(Operations(bot))

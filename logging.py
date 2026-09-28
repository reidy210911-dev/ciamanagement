import discord
from discord.ext import commands

class Logging(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        @commands.Cog.listener()
        async def on_message(self, message):
            print(f'Message from {message.author}: {message.content}')

            async def setup(bot):
                await bot.add_cog(Logging(bot))

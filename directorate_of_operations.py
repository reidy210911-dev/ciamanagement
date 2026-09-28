import discord
from discord.ext import commands
from discord.ui import Button, View

class DirectorateOfOperations(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        @commands.command()
        async def operation(self, ctx):
            await ctx.send('Operation command')

            @commands.command()
            async def training(self, ctx):
                await ctx.send('Training command')

                @commands.command()
                async def ieot_event(self, ctx):
                    await ctx.send('IEOT event command')

                    async def setup(bot):
                        await bot.add_cog(DirectorateOfOperations(bot))

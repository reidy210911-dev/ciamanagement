import discord
from discord.ext import commands
from discord.ui import Button, View

class TrainingAcademy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        @commands.command()
        async def training(self, ctx):
            await ctx.send('Training command')

            @commands.command()
            async def promotion(self, ctx):
                await ctx.send('Promotion command')

                @commands.command()
                async def demotion(self, ctx):
                    await ctx.send('Demotion command')

                    async def setup(bot):
                        await bot.add_cog(TrainingAcademy(bot))

import discord
from discord.ext import commands
from discord.ui import Button, View

class DirectorateOfAnalysis(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        @commands.command()
        async def intelligence_report(self, ctx):
            await ctx.send('Intelligence report command')

            @commands.command()
            async def investigation(self, ctx):
                await ctx.send('Investigation command')

                @commands.command()
                async def case(self, ctx):
                    await ctx.send('Case command')

                    async def setup(bot):
                        await bot.add_cog(DirectorateOfAnalysis(bot))

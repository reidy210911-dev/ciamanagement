import discord
from discord.ext import commands
from discord.ui import Button, View

class Statistics(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        @commands.command()
        async def stats(self, ctx):
            await ctx.send('Statistics command')

            @commands.command()
            async def announcement(self, ctx):
                await ctx.send('Announcement command')

                @commands.command()
                async def ticket(self, ctx):
                    await ctx.send('Ticket command')

                    async def setup(bot):
                        await bot.add_cog(Statistics(bot))

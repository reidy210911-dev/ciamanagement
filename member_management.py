import discord
from discord.ext import commands
from discord.ui import Button, View

class MemberManagement(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        @commands.command()
        async def application(self, ctx):
            await ctx.send('Application command')

            @commands.command()
            async def warning(self, ctx):
                await ctx.send('Warning command')

                @commands.command()
                async def strike(self, ctx):
                    await ctx.send('Strike command')

                    @commands.command()
                    async def loa(self, ctx):
                        await ctx.send('LOA command')

                        @commands.command()
                        async def staff_report(self, ctx):
                            await ctx.send('Staff report command')

                            async def setup(bot):
                                await bot.add_cog(MemberManagement(bot))

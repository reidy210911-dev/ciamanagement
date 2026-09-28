import discord
from discord.ext import commands
from discord.ui import Button, View

class Cybersecurity(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        @commands.command()
        async def cybersecurity_record(self, ctx):
            await ctx.send('Cybersecurity record command')

            @commands.command()
            async def background_check(self, ctx):
                await ctx.send('Background check command')

                @commands.command()
                async def blacklist(self, ctx):
                    await ctx.send('Blacklist command')

                    async def setup(bot):
                        await bot.add_cog(Cybersecurity(bot))

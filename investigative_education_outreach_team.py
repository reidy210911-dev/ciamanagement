import discord
from discord.ext import commands
from discord.ui import Button, View

class InvestigativeEducationOutreachTeam(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        @commands.command()
        async def ieot_event(self, ctx):
            await ctx.send('IEOT event command')

            @commands.command()
            async def activity_tracking(self, ctx):
                await ctx.send('Activity tracking command')

                @commands.command()
                async def quota(self, ctx):
                    await ctx.send('Quota command')

                    async def setup(bot):
                        await bot.add_cog(InvestigativeEducationOutreachTeam(bot))

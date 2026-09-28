import discord
from discord.ext import commands
from discord.ui import Button, View

class AuditLogs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        @commands.command()
        async def audit_log(self, ctx):
            await ctx.send('Audit log command')

            async def setup(bot):
                await bot.add_cog(AuditLogs(bot))

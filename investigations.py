import discord
from discord.ext import commands

class Investigations(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        @commands.command()
        async def investigate(self, ctx, member: discord.Member, reason: str):
            await ctx.send(f'Investigation started for {member.mention} for {reason}')

            async def setup(bot):
                await bot.add_cog(Investigations(bot))

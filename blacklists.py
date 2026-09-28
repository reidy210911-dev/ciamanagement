import discord
from discord.ext import commands

class Blacklists(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        @commands.command()
        async def blacklist(self, ctx, member: discord.Member, reason: str):
            await ctx.send(f'{member.mention} has been blacklisted for {reason}')

            async def setup(bot):
                await bot.add_cog(Blacklists(bot))

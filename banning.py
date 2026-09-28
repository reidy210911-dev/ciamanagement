import discord
from discord.ext import commands

class Banning(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        @commands.command()
        async def ban(self, ctx, member: discord.Member, reason: str):
            await member.ban(reason=reason)
            await ctx.send(f'{member.mention} has been banned for {reason}')

            async def setup(bot):
                await bot.add_cog(Banning(bot))

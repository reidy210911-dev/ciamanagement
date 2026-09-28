import discord
from discord.ext import commands

class Management(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        @commands.command()
        async def manage(self, ctx, member: discord.Member, action: str):
            await ctx.send(f'Management action {action} taken for {member.mention}')

            async def setup(bot):
                await bot.add_cog(Management(bot))

import discord
from discord.ext import commands

class Promotions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        @commands.command()
        async def promote(self, ctx, member: discord.Member, role: discord.Role):
            await member.add_roles(role)
            await ctx.send(f'{member.mention} has been promoted to {role.name}')

            async def setup(bot):
                await bot.add_cog(Promotions(bot))

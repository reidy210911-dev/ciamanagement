import discord
from discord.ext import commands

class Demotions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        @commands.command()
        async def demote(self, ctx, member: discord.Member, role: discord.Role):
            await member.remove_roles(role)
            await ctx.send(f'{member.mention} has been demoted from {role.name}')

            async def setup(bot):
                await bot.add_cog(Demotions(bot))

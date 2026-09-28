import discord
from discord.ext import commands

class LeaveOfAbsence(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        @commands.command()
        async def loa(self, ctx, member: discord.Member, reason: str):
            await ctx.send(f'{member.mention} has been placed on leave of absence for {reason}')

            @commands.command()
            async def return_from_loa(self, ctx, member: discord.Member):
                await ctx.send(f'{member.mention} has returned from leave of absence')

                async def setup(bot):
                    await bot.add_cog(LeaveOfAbsence(bot))

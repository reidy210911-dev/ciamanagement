import discord
from discord.ext import commands

class Cases(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        @commands.command()
        async def case(self, ctx, case_name: str, case_details: str):
            await ctx.send(f'Case {case_name} created with details: {case_details}')

            async def setup(bot):
                await bot.add_cog(Cases(bot))

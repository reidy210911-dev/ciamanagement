import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {{bot.user}}')

    async def has_admin_role(ctx):
        admin_role = discord.utils.get(ctx.guild.roles, id=int(os.getenv('ADMIN_ROLE_ID')))
        return admin_role in ctx.author.roles

        async def has_moderator_role(ctx):
            moderator_role = discord.utils.get(ctx.guild.roles, id=int(os.getenv('MODERATOR_ROLE_ID')))
            return moderator_role in ctx.author.roles

            async def has_staff_role(ctx):
                staff_role = discord.utils.get(ctx.guild.roles, id=int(os.getenv('STAFF_ROLE_ID')))
                return staff_role in ctx.author.roles

                async def has_ieot_role(ctx):
                    ieot_role = discord.utils.get(ctx.guild.roles, id=int(os.getenv('IEOT_ROLE_ID')))
                    return ieot_role in ctx.author.roles

                    async def has_doo_role(ctx):
                        doo_role = discord.utils.get(ctx.guild.roles, id=int(os.getenv('DOO_ROLE_ID')))
                        return doo_role in ctx.author.roles

                        async def has_doa_role(ctx):
                            doa_role = discord.utils.get(ctx.guild.roles, id=int(os.getenv('DOA_ROLE_ID')))
                            return doa_role in ctx.author.roles

                            async def has_cybersecurity_role(ctx):
                                cybersecurity_role = discord.utils.get(ctx.guild.roles, id=int(os.getenv('CYBERSECURITY_ROLE_ID')))
                                return cybersecurity_role in ctx.author.roles

                                @bot.command(name='admin_command')
                                @commands.check(has_admin_role)
                                async def admin_command(ctx):
                                    await ctx.send('This is an admin command.')

                                    @bot.command(name='moderator_command')
                                    @commands.check(has_moderator_role)
                                    async def moderator_command(ctx):
                                        await ctx.send('This is a moderator command.')

                                        @bot.command(name='staff_command')
                                        @commands.check(has_staff_role)
                                        async def staff_command(ctx):
                                            await ctx.send('This is a staff command.')

                                            @bot.command(name='ieot_command')
                                            @commands.check(has_ieot_role)
                                            async def ieot_command(ctx):
                                                await ctx.send('This is an IEOT command.')

                                                @bot.command(name='doo_command')
                                                @commands.check(has_doo_role)
                                                async def doo_command(ctx):
                                                    await ctx.send('This is a DOO command.')

                                                    @bot.command(name='doa_command')
                                                    @commands.check(has_doa_role)
                                                    async def doa_command(ctx):
                                                        await ctx.send('This is a DOA command.')

                                                        @bot.command(name='cybersecurity_command')
                                                        @commands.check(has_cybersecurity_role)
                                                        async def cybersecurity_command(ctx):
                                                            await ctx.send('This is a Cybersecurity command.')

                                                            @bot.event
                                                            async def on_command_error(ctx, error):
                                                                if isinstance(error, commands.CheckFailure):
                                                                    await ctx.send('You do not have the required role to use this command.')

                                                                    bot.run(os.getenv('DISCORD_TOKEN'))

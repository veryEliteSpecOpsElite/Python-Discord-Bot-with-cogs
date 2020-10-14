from discord.ext import commands
import discord
from discord.ext.commands import has_permissions

class Mod(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.command(
        name='kick',
        description='Kick user.',
        aliases=[]
    )
    @has_permissions(administrator=True)
    async def kick(self, ctx, member: discord.Member):
        if True:
            guild=ctx.guild
            try:
                await member.kick()
                await ctx.send('{} has been kicked by {}.'.format(member, ctx.author))
            except Exception as e:
                await ctx.send(f'```{e}```')
        else:
            return

    @commands.command(
        name='ban',
        description='Ban user',
        aliases=[]
    )
    async def ban(self, ctx, member:discord.Member):
        if ctx.author.server_permissions.administrator:
            guild=ctx.guild
            try:
                await member.ban()
                await ctx.send('{} has been banned.'.format(member))
            except Exception as e:
                await ctx.send(f'```{e}```')
        else:
            return
    
    @commands.command(
        name='unban',
        description='Unban user (doenst work)',
        aliases=[]
    )
    async def unban(self, ctx, member:discord.Member):
        if ctx.author.server_permissions.administrator:
            guild=ctx.guild
            try:
                await member.unban()
                await ctx.send('{} has been unbanned.'.format(member))
            except Exception as e:
                await ctx.send('```{}```'.format(e))
        else:
            return


def setup(bot):
    bot.add_cog(Mod(bot))

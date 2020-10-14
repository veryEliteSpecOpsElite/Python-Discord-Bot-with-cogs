from discord.ext import commands
import discord
import jishaku

class Owner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name='reload_cog',
        description='Reload cog (owner only)',
        aliases=['r_c', 'r-c']
    )
    async def reload_cog(self, ctx):
        if ctx.author.id == 640203987437748246:
            msg=ctx.message.content.split()
            msg.pop(0)
            msg=' '.join(msg)
            cogs = ['cogs.basic', 'cogs.help', 'cogs.b_info', 'cogs.invite', 'cogs.roles', 'cogs.misc', 'cogs.tags', 'cogs.mod', 'cogs.gb', 'cogs.eval', 'cogs.code', 'cogs.owner_only']
            if msg in cogs:
                c=await ctx.send('Loading cog...')
                try:
                    self.bot.unload_extension(msg)
                    self.bot.load_extension(msg)
                    await c.edit(content=':white_check_mark: Reloaded cog `{}`.'.format(msg))
                except Exception as e:
                    await c.edit(content=':regional_indicator_x: Something went wrong:\n```{}```'.format(e))
            else:
                await ctx.send(':regional_indicator_x: `{}` is not a cog.'.format(msg))
        else:
            return

    @commands.command(
        name='set_status',
        description='set bot status (owner only)',
        aliases=['s_s', '$_$']
    )
    async def set_status(self, ctx):
        if ctx.author.id == 640203987437748246:
            ctx.message.content = ctx.message.content.split()
            ctx.message.content.pop(0)
            msg=' '.join(ctx.message.content)
            game=discord.Game(msg)
            await self.bot.change_presence(status=discord.Status.online, activity=game)
            
            await ctx.send(content='Status changed to:\nStatus: `discord.Status.online`\nActivity: `{}`'.format(game))
        else:
            await ctx.send('`set_status` is an owner only command.')
            return

    @commands.command(
        name='_jsk',
        description='(Not real jsk command) jsk command, owner only.'
    )
    async def __jsk(self, ctx):
        await ctx.send('This is not the real jsk command. The real one is owner only.')
        return

    @commands.command(
        name='leave',
        description='Leave current server.'
    )
    async def leave(self, ctx):
        if ctx.author.id==640203987437748246:
            await ctx.guild.leave()
        else:
            return

    

def setup(bot):
    bot.add_cog(Owner(bot))

from discord.ext import commands
import discord, discord.utils


class Roles(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.command(
        name='add_role',
        description='add new role.',
        aliases=['a_r', 'a r']
    )
    async def add_role(self, ctx, role:discord.Role):
        member = ctx.message.author
        ctx.message.content = ctx.message.content.split()
        ctx.message.content.pop(0)
        ctx.message.content=" ".join(ctx.message.content)
        try:
            await member.add_roles(member, role)
            await ctx.send('Role created.')
        except Exception as e:
            await ctx.send('```{}```'.format(e))

    @commands.command(
        name='roles',
        description='View all roles in server.',
        aliases=['rs']
    )
    async def view_roles(self, ctx):
        empty=''
        for role in ctx.guild.roles:
            empty+=role.name
            empty+='\n'
        await ctx.send('```{}```'.format(empty))


    @commands.command(
        name='create_role',
        description='create a new role.',
        aliases=['c_r']
    )
    async def create_role(self, ctx):
        guild=ctx.guild
        ctx.message.content=ctx.message.content.split()
        ctx.message.content.pop(0)
        addto=' '.join(ctx.message.content) 
        msg=await ctx.send('```Creating role...```')
        await guild.create_role(name='{}'.format(addto))
        await msg.edit(content='```Role created.\nName: {}```'.format(addto))
        print(ctx.guild.roles)



    


def setup(bot):
    bot.add_cog(Roles(bot))

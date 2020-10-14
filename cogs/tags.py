from discord.ext import commands
import discord, sys
from datetime import datetime

tags = []

class Tags(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.command(
        name='tags',
        description='View all tags.',
        aliases=['ts']
    )
    async def all_tags(self, ctx):
        messages = '__Tags__\n'
        if len(tags) > 0:
            for tag in tags:
                messages += '{}, '.format(tag[0])

        else:
            messages += '**No tags**\n*Use create_tag to create one.*'
        await ctx.send(messages)
    
    @commands.command(
        name='create_tag',
        description='Create a new tag.',
        aliases=[]
    )
    async def create_tag(self, ctx):
        def check(ms):
            return ms.channel == ctx.message.channel and ms.author == ctx.message.author
        tag = []
        msg = ctx.message.content.split()
        if len(msg) == 2:
            title = msg[1]
            tag.append(title)
        elif len(msg) > 2:
            await ctx.send('Tag one word only.')
            return
        else:
            await ctx.send('Missing: `name`')
            return
        await ctx.send('Content:')
        content=await self.bot.wait_for('message', check=check)
        tag.append(content.content)
        await ctx.send('Tag created :white_check_mark:')
        tags.append(tag)
        print(tag)



    @commands.command(
        name='clear_tags',
        description='Clears all tags.',
        aliases=[]
    )
    async def clear_tags(self, ctx):
        msg = await ctx.send('Clearing tags...')
        tags=[]
        await msg.edit(content='Tags deleted. Tags: `{}`'.format(tags))

    @commands.command(
        name='tag',
        description='View cotnent of a tag.',
        aliases=[]
    )
    async def tag(self, ctx):
        message = ctx.message.content.split()
        message.pop(0)
        message = ' '.join(message)
        for tag in tags:
            try:
                if message == tag[0]:
                    print(tag)
                    c=tag[0]
                    tag.pop(0)
                    await ctx.send(' '.join(tag))
                    tag.insert(0, c)
                else:
                    pass
            except:
                e=sys.exc_info()[0]
                await ctx.send('{}'.format(e))

    

            





def setup(bot):
    bot.add_cog(Tags(bot))

from discord.ext import commands
import discord, time, sys
from discord.ext.commands import has_permissions

bots = []

class gb(commands.Cog, name='Good_Bot'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name='addbot',
        description='Add a bot to contest.',
        aliases=['ab']
    )
    async def add_bot(self, ctx, member: discord.Member):
        if member.bot:
            bot = ['{}'.format(member.name), 0]
            bots.append(bot)
            await ctx.send('{} has been added to the contest!'.format(member.name))
            print(bots)
        else:
            await ctx.send('{} is not a bot.'.format(member))
            return


    @commands.command(
        name='botstat',
        description='View bot\'s stats for contest.',
        aliases=['_bs']
    )
    async def _bot_stats_(self, ctx, member:discord.Member):
        try:
            for i in range(len(bots)):
                if member.name in bots[i]:
                    embed=discord.Embed(
                        title='{}'.format(member.name),
                        color=0x000000
                    )
                    embed.add_field(
                        name='Points:', value='{}'.format(bots[i][1]), inline=False
                    )
                    await ctx.send(embed=embed)
                    return
            await ctx.send('Bot not found.')
        except Exception as e:
            await ctx.send('```{}```'.format(e))

    @commands.command(
        name='goodbot',
        description='Give a point to a bot.',
        aliases=['gb']
    )
    async def good_bot(self, ctx, member:discord.Member):
        msg = ctx.message.content.split()
        if True:
            for i in range(len(bots)):
                if bots[i][0] == member.name:
                    bots[i][1] += 1
                    await ctx.send('{} has had a point added! {} now has {} points.'.format(member, member, bots[i][1]))
                    print(bots[i])
                    return
            await ctx.send('Bot not found.')
        if False:
            for i in range(len(bots)):
                if bots[i][0] == member.name and int(msg[2])<=10:
                    try:
                        bots[i][1] += int(msg[2])
                        await ctx.send('{} has had a {} point(s) added! {} now has {} points.'.format(member, msg[2], member, bots[i][1]))
                        print(bots[i])
                        return
                    except:
                        await ctx.send('```{}```'.format(sys.exc_info()))
                        return
                elif int(msg[2]) > 10:
                    await ctx.send(':x: Error\nMax points given at a time: 10')
                    return
            await ctx.send('Bot not found.')


    @commands.command(
        name='badbot',
        description='Take a point away from a bot.',
        aliases=['bb']
    )
    async def badbot(self, ctx, member:discord.Member):
        msg = ctx.message.content.split()
        if True:
            for i in range(len(bots)):
                if member.name in bots[i]:
                    bots[i][1] -= 1
                    await ctx.send('{} has lost a point! {} now has {} points.'.format(member, member, bots[i][1]))
                    return
            await ctx.send('Bot not found.')
        else:
            for i in range(len(bots)):
                if member.name in bots[i] and int(msg[2]) <= 10:
                    try:
                        bots[i][1] -= int(msg[2])
                        await ctx.send('{} has lost {} point(s)! {} now has {} points.'.format(member, msg[2], member, bots[i][1]))
                        return
                    except:
                        await ctx.send('```{}```'.format(sys.exc_info()))
                        return
                elif int(msg[2]) > 10:
                    await ctx.send(':x: Error\nMax points taken at a time: 10')
                    return
            await ctx.send('Bot not found.')


    @commands.command(
        name='add_all',
        description='Add all bots in the server to contest.',
        aliases=['_a']
    )
    @has_permissions(administrator=True)
    async def add_all(self, ctx):
        msg = await ctx.send('\U0000231b Finding and adding bots...')
        done = 0
        guild = ctx.guild
        for member in guild.members:
            if member.bot and member.id != 665674407611727915:
                bots.append([member.name, 0])
                done += 1
        time.sleep(0.2)
        await msg.edit(content='\U00002705 Bots successfully added: {}'.format(done))

    @commands.command(
        name='all_bots',
        description='View all bots in contest.',
        aliases=['_a_b']
    )
    async def _view(self, ctx):
        string = ""
        for i in range(len(bots)):
            string += "**{}:** {}\n".format(bots[i][0], bots[i][1])
        embed=discord.Embed(title='All bots', description=string, color=0x000000)
        await ctx.send(embed=embed)

    

        
                    

def setup(bot):
    bot.add_cog(gb(bot))

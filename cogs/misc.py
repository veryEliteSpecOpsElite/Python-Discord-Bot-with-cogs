from discord.ext import commands
import discord, csv, random, asyncio, binascii, codecs
from discord.ext.commands.cooldowns import BucketType




colors=[0x000000,0xFFFFFF,0x1ABC9C,0x2ECC71,0x3498DB,0x9B59B6,0xE91E63,0xF1C40F,0xE67E22,0xE74C3C,0x95A5A6,0x34495E,0x34495E,0x11806A,0x11806A,0x1F8B4C,0x206694,0x71368A,0xAD1457,0xC27C0E,0xA84300,0x7289DA0,0x99AAB5]








class Misc(commands.Cog, name='Misc/Fun'):
    def __init__(self, bot):
        self.bot=bot

    @commands.command(
        name='nick_set',
        description='Change bot nick.',
        aliases=['n_s', 'ns']
    )
    async def change_nick(self, ctx):
        ctx.message.content=ctx.message.content.split()
        if len(ctx.message.content) > 1:
            ctx.message.content.pop(0)
            nick=' '.join(ctx.message.content)
            if len(nick)<=32:
                await ctx.guild.get_member(self.bot.user.id).edit(nick=nick)
                await ctx.send('Nick changed to `{}`.'.format(nick))
            else:
                await ctx.send('Name too long. Max len: 32')
        else:
            await ctx.send('Missing: `name`')

    @commands.command(
        name='annoy_someone',
        description='Nonems',
        aliases=['iass']
    )
    async def annoy_someone(self, ctx):
        ff=open('blank.csv')
        readed=csv.reader(ff)
        quoted=list(readed)
        r=random.randint(0, 178)
        sent = await ctx.send('```{}```'.format(quoted[r]))
        await sent.add_reaction(emoji='\U0001f44d')
        await sent.add_reaction(emoji='\U0001f44e')


        
    @commands.command(
        name='xkcd',
        description='Show an xkcd comic.',
        aliases=['xxxx']
    )
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def xkcd(self, ctx):
        def check(ms):
            return ms.channel == ctx.message.channel and ms.author == ctx.message.author
        try:
            msg = ctx.message.content.split()
            if len(msg) == 1:
                while True:
                    r=random.randint(1, 2257)
                    c=await ctx.send('https://xkcd.com/{}/\nUse `next` `prev` and `rand` to navigate comics.'.format(r))
                    react = await self.bot.wait_for('message', check=check)
                    if react.content == 'next':
                        await c.edit(content='https://xkcd.com/{}/'.format(r+1))
                    elif react.content == 'prev':
                        await c.edit(content='https://xkcd.com/{}/'.format(r-1))
                    elif react.content == 'rand':
                        r=random.randint(1, 2257)
                        await c.edit(content='https://xkcd.com/{}/'.format(r))
                    else:
                        break
                else:
                    num = int(msg[1])
                    if num <= 2257 and num >= 1:
                        await ctx.send('https://xkcd.com/{}/'.format(str(num)))
        except discord.ext.commands.errors.CommandOnCooldown as c:
            await ctx.send('@{}, {}'.format(ctx.author, c))

    @commands.command(
        name='wiki',
        description='Search wikipedia for something.'
    )
    async def search(self, ctx):
        if len(ctx.message.content.split())>1:
            msg=ctx.message.content.split()
            msg.pop(0)
            msg='_'.join(msg)
            #print(msg)
            await ctx.send('https://en.wikipedia.org/wiki/{}'.format(msg.title()))
        else:
            await ctx.send(':regional_indicator_x: Something went wrong.\nProper format: ut.wiki <query>')

    

    @commands.command(
        name='color',
        description='Show a random color in hex.',
        aliases=[]
    )
    async def rand_color(self, ctx):
        x=random.choice(colors)
        try:
            c=hex(x)
            ff=str(c)
            ff=list(ff)
            ff.pop(0)
            ff.pop(0)
            ff.insert(0, '#')
            ff=''.join(ff)
            embed=discord.Embed(title='', description='**{}**'.format(ff), color=int(x))
            embed.add_field(name='<--', value='*Look to the left to see color, not here!*', inline=False)
            await ctx.send(embed=embed)
        except Exception as e:
            await ctx.send('```{}```'.format(e))

    @commands.command(
        name='profile',
        description='View stats of user.',
        aliases=['prof']
    )
    async def profile_user(self, ctx, member:discord.Member):
        try:
            await self.bot.fetch_user(ctx.author.id)
            embed=discord.Embed(title='', color=0x000000)
            url=member.avatar_url
            embed.set_thumbnail(url=url)
            embed.set_author(
                name=member,
                icon_url=member.avatar_url
            )
            on_mobile=''
            if member.is_on_mobile():
                on_mobile = 'Mobile :iphone:'
            else:
                on_mobile = 'PC :computer:'
            activity = ''
            try:
                if member.activity.name == 'Custom Status':
                    activity = member.activity.name
                else:
                    activity = 'None'
            except:
                activity = 'None'
            embed.add_field(name='User Info', value='**ID:** {}\n**Discriminator:** #{}\n**Nickname:** `{}`\n**Full name:** {}'.format(member.id, member.discriminator, member.nick, member.name), inline=False)
            embed.add_field(name='Status', value='**Status:** {}\n**Activity:** {}\n**Platform:** {}'.format(member.status, activity, on_mobile), inline=True)
            embed.add_field(name='Misc', value='**Bot:** {}\n**Number of roles:** {}\n**Joined:** {}'.format(member.bot, len(member.roles), member.joined_at), inline=True)
            roles=[]
            for role in member.roles:
                roles.append(role.name)
            roles = ', '.join(roles)
            embed.add_field(name='__Roles:__', value=roles, inline=False)
            await ctx.send(embed=embed)
        except Exception as e:
            await ctx.send(f'```{e}```')

    

    @commands.command(
        name='create_channel',
        description='Create a new channel (owner only)',
        aliases=[]
    )
    async def create_channel(self, ctx):
        if ctx.author.server_permissions.administrator:
            guild=ctx.message.guild
            mm=ctx.message.content.split()
            mm.pop(0)
            mm=' '.join(mm)
            await guild.create_text_channel(mm)
            msg=await ctx.send('Creating channel...')
            await asyncio.sleep(0.75)
            await msg.edit(content='Channel created.')
        else:
            await ctx.send('`create_channel` is an owner only command.')
            return




    @commands.command(
        name='cogs',
        description='View all bots cogs.',
        aliases=[]
    )
    async def view_cogs(self, ctx):
        try:
            await ctx.send('{}'.format(self.bot.cogs))
        except Exception as e:
            await ctx.send('```{}```'.format(e))

    @commands.command(
        name='user_av',
        description='See avatar of user.',
        aliases=['u_a']
    )
    async def show_av(self, ctx, member: discord.Member):
        embed=discord.Embed(title="{}'s avatar".format(member), color=0x000000)
        embed.set_author(
            name=member.name,
            icon_url=member.avatar_url
        )
        url=member.avatar_url
        embed.set_image(url=url)
        await ctx.send(embed=embed)

    @commands.command(
        name='urban',
        description='View urban dictionary definition of word.',
        aliases=[]
    )
    async def urban_def(self, ctx):
        msg = ctx.message.content.split()
        if len(msg) == 2:
            await ctx.send('https://www.urbandictionary.com/define.php?term={}'.format(msg[1]))
        elif len(msg) > 2:
            await ctx.send(':x: Something went wrong. Try this:\n`ut.urban [insert __one__ word]`')
        else:
            await ctx.send('```list index out of range.```')

    

    

    @commands.command(
        name='a sentence in binary',
        description='Get "a sentence in binary" in binary.',
        aliases=['asib']
    )
    async def a_sentence_in_binary(self, ctx):
        def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
            bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
            return bits.zfill(8*((len(bits) + 7) // 8))
        text='a sentence in binary'
        msg=text_to_bits(text)
        await ctx.send(msg)



    


    

    















        
        


def setup(bot):
    bot.add_cog(Misc(bot))
        

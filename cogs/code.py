from discord.ext import commands
import discord, binascii

class Code(commands.Cog, name='Conversion'):
    def __init__(self, bot):
        self.bot=bot

    @commands.command(
        name='hex',
        description='Get a number/char/string in hexformat.'
    )
    async def _hex_(self, ctx, num):
        try:
            ori=num
            try:
                h=hex(int(num))
            except:
                dd = []
                for n in num:
                    dd.append(ord(n))
                h=''
                print(dd)
                for d in dd:
                    h+=str(d)
                h=int(h)
                h=hex(h)

            embed=discord.Embed(
                title='Hexadecimal format:',
                description='{} -> **{}**'.format(str(ori), h),
                color=0x000000
            )
            await ctx.send(embed=embed)
        except Exception as e:
            await ctx.send(':regional_indicator_x: Something went wrong.\n```{}```'.format(e))

    @commands.command(
        name='unicode',
        description='Get unicode of string. (Doesn\'t work)',
        aliases=['uni']
    )
    async def uni(self, ctx):
        msg = ctx.message.content.split()
        msg.pop(0)
        msg = ' '.join(msg)
        _o_ = msg
        sent = msg.encode('utf-8', 'surrogatepass')
        embed=discord.Embed(title='Unicode:', description='{} -> **{}**'.format(_o_, sent), color=0x00000)
        await ctx.send(embed=embed)

    @commands.command(
        name='rand_ascii',
        description='Get a random symbol in ascii.',
        aliases=['r_as']
    )
    async def rand_ascii(self, ctx):
        symbols = [
            'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','!','@','#','$','%','^','&','*','(',')','1','2','3','4','5','6','7','8','9','0','<','>',',','.','/', '\\', '?', '{', '[', '}', ']', '|', '=', '+'
        ]
        symbol = random.choice(symbols)
        embed=discord.Embed(title='Ascii:', description='{} -> **{}**'.format(symbol, ord(symbol)), color=0x000000)
        await ctx.send(embed=embed)


    

    @commands.command(
        name='ascii',
        description='Get ascii code for <text>.',
        aliases=[]
    )
    async def view_ascii(self, ctx):
        msg = ctx.message.content.split()
        msg.pop(0)
        original = ' '.join(msg)
        msg = ' '.join(msg)
        msg = list(msg)
        to_send = ''
        for x in msg:
            to_send += str(ord(x))
            to_send += ' '
        embed=discord.Embed(title='Ascii:', description='{} -> **{}**'.format(original, to_send), color=0x000000)
        await ctx.send(embed=embed)

    @commands.command(
        name='binary',
        description='Get binary of string.',
        aliases=['bin']
    )
    async def binary(self, ctx):
        def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
            bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
            return bits.zfill(8*((len(bits) + 7) // 8))
        msg = ctx.message.content.split()
        msg.pop(0)
        msg = ' '.join(msg)
        sent = text_to_bits(msg)
        embed=discord.Embed(title='Binary', description='{} -> **{}**'.format(msg, sent))
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Code(bot))

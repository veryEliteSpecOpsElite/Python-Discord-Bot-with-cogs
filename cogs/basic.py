from discord.ext import commands
import time, discord, datetime, csv, math


def truncate(number, digits) -> float:
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper

pingtimes = []


class Basic(commands.Cog, name='Ping/latency'):
    def __init__(self, bot):
        self.bot=bot

    @commands.command(
        name='ping_times',
        description='Get all ping times. (not now, while bot under construction.)',
        aliases=['p_t']
    )
    async def pings(self, ctx):
        await ctx.trigger_typing()
        times=[]
        c=open('times.csv')
        cc=csv.reader(c)
        ccc=list(cc)
        for cccc in ccc:
            times.append(cccc)
        embed=discord.Embed(title='Ping times', color=0x000000)
        embed.add_field(name=None, value=ccc)
        await ctx.send(embed=embed)
        

    @commands.command(
        name='ping',
        description='Test your connection.',
        aliases=['p']
    )
    async def ping_cmd(self, ctx):
        msg = await ctx.send('Pinging...')
        time_1 = time.perf_counter()
        await ctx.trigger_typing()
        time_2 = time.perf_counter()
        ping = round((time_2-time_1)*1000)
        await msg.edit(content=':ping_pong: Pong. Time round-trip: `{}ms`.'.format(ping))
        with open('times.csv', 'a') as foo:
            fooo=csv.writer(foo, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            fooo.writerow([str(ping)])

    @commands.command(
        name='latency',
        description='Get bot latency.',
        aliases=['_l_']
    )
    async def get_latency(self, ctx):
        l=self.bot.latency*1000
        l=truncate(l, 2)
        await ctx.send('Latency: `{}ms`'.format(l))


    

        

    



    
        


    

def setup(bot):
    bot.add_cog(Basic(bot))



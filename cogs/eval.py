from discord.ext import commands
import inspect, pyperclip, discord, time, asyncio, math

def truncate(number, digits) -> float:
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper


class Eval(commands.Cog, name='REPL'):
    def __init__(self, bot):
        self.bot=bot

    @commands.command(
        name='eval',
        description='Interactive Python 3.x shell. (Only perform basic operations)\n`uteval <code>` (evaluates code)',
        aliases=[]
    )
    async def eval_(self, ctx, code: str):
        if ctx.guild.id == 641124805235572776:
            prof = time.process_time()
            await ctx.trigger_typing()
            code = code.strip('` ')
            result = None
            env = {
            'bot': self.bot,
            'ctx': ctx,
            'message': ctx.message,
            'server': ctx.message.guild,
            'channel': ctx.message.channel,
            'author': ctx.message.author
            }

            env.update(globals())

            try:
                result = eval(code, env)
                if inspect.isawaitable(result):
                    result = await result
                    print(result)
            except Exception as e:
                await ctx.send('```%s```'%(e))
                return
            embed=discord.Embed(
                title='',
                color=0x000000
            )
            embed.set_author(name='Requested by: {}'.format(ctx.author), icon_url = ctx.author.avatar_url)
            embed.add_field(name='Command: ', value='```{}```'.format(code), inline=True)
            embed.add_field(
                name='Result:',
                value='```{}```'.format(result),
                inline=False
            )
            prof=truncate(prof, 2)
            embed.set_footer(text='That took: {}ms'.format(str(prof)))
            await ctx.send(embed=embed)
        else:
            await ctx.send('You can only use this command in the bots home server.')
            return
    
    @commands.command(
        name='repl',
        description='Launch a repl session, go idle for 20 seconds, while auto quit.'
    )
    async def repl_session(self, ctx):
        def check(ms):
            return ms.channel == ctx.message.channel and ms.author == ctx.message.author
        if ctx.guild.id == 641124805235572776:
            env = {
                'bot': self.bot,
                'ctx': ctx,
                'message': ctx.message,
                'server': ctx.message.guild,
                'channel': ctx.message.channel,
                'author': ctx.message.author
            }

            env.update(globals())
            hhuh_ = await ctx.send('Starting repl session...')
            await asyncio.sleep(0.3)
            await hhuh_.edit(content='REPL session started. :white_check_mark:')
            while True:
                try:
                    response = await self.bot.wait_for('message', check=check, timeout=10.0 * 2.0)
                except asyncio.TimeoutError:
                    msg=await ctx.send('Exiting REPL session.')
                    await msg.edit(content='Successfully quit. (Idle timeout 20 seconds)')
                    break
                msg = await self.bot.wait_for('message', check=check)
                if msg == 'exit':
                    msg=ctx.send('Stopping...')
                    print('Stopped.')
                    time.sleep(0.1)
                    await msg.edit('Done :white_check_mark:')
                    break
                code = msg.content.strip('` ')
                try:
                    result = eval(code, env)
                    if inspect.isawaitable(result):
                        result = await result
                        print(result)
                except Exception as e:
                    await ctx.send('```%s```'%(e))
                    return
                await ctx.send('```{}```'.format(result))
            return
        else:
            await ctx.send('You can only use this command in the bots home server.')
            return
    @commands.command(
        name='operations',
        description='View all available operations.'
    )
    async def view_all(self, ctx):
        await ctx.send('Operations (for repl session, eval):\n-Add (+)\n-Subtract (-)\n-Multiply (*)\n-Divide (/)\n-Exponent (**)\n-Modulo (%)\n-Integer divide (//)')

    @commands.command(
        name='exec',
        description='Perform `exec()` function.'
    )
    async def _exec_(self, ctx, code:str):
        if ctx.guild.id == 641124805235572776:
            env = {
                'bot': self.bot,
                'ctx': ctx,
                'message': ctx.message,
                'server': ctx.message.guild,
                'channel': ctx.message.channel,
                'author': ctx.message.author
            }
            env.update(globals())
            try:
                result = eval(code, env)
                if inspect.isawaitable(result):
                    result = await result
            except Exception as e:
                await ctx.send(':regional_indicator_x: Something went wrong:\n```{}```'.format(e))
                return
            await ctx.send(f'```{result}```')
        else:
            await ctx.send('You can only use this command in the bots home server.')
            return

        


def setup(bot):
    bot.add_cog(Eval(bot))

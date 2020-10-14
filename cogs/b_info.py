from discord.ext import commands
import discord, time, csv, discord.utils, math


def truncate(number, digits) -> float:
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper


class Stuff(commands.Cog, name='Info'):
    def __init__(self, bot):
        self.bot=bot

    @commands.command(
        name='info',
        description='Shows info on bot.',
        aliases=['ii']
    )
    async def testing(self, ctx):
        user = self.bot.get_user(self.bot.owner_id)
        x=open('times.csv')
        xx=csv.reader(x)
        xxx=list(xx)
        all_times = 0
        for x in xxx:
            c = []
            c.append(x[0])
            c[0] = int(c[0])
            all_times += c[0]
        time = all_times / len(xxx)
        time = str(time)
        time = list(time)
        for i in range(len(time)-4):
            time.pop()
        _time = ''.join(time)
        embed=discord.Embed(title='', color=0x000000)
        url=self.bot.user.avatar_url
        user = self.bot.get_user(665674407611727915)
        embed.set_author(
            name=user.name,
            icon_url=url
        )
        embed.set_thumbnail(url=url)
        users = 0
        for guild in self.bot.guilds:
            users += len(guild.members)
        commands = 0
        for command in self.bot.commands:
            commands += 1
        lat = self.bot.latency*1000
        l=int(lat)
        l=truncate(l, 2)
        lat=str(l)
        embed.add_field(name='__Stats__', value='**Avg ping time:** {}ms\n**Websocket latency:** {}ms\n**Num of guilds:** {}\n**Users:** {}\n**Commands:** {}\n**Cooldown:** 5s'.format(_time, lat, len(self.bot.guilds), users, commands), inline=True)
        embed.add_field(name='__Code__', value='**discord.py version:** {}\n**Lines:** >720\n**Files:** >15\n**Cogs:** {}\n**Functions:** >47'.format(discord.__version__, len(self.bot.cogs)), inline=True)
        embed.add_field(name='__Created by:__', value=user, inline=False)
        embed.add_field(name='Links:', value='[**invite**](https://discordapp.com/api/oauth2/authorize?client_id=665674407611727915&permissions=8&scope=bot)  **|** [**source**](https://github.com/insert-ctrl/discord-utils-src)', inline=False)
        embed.set_footer(text='ID: {} | Made by {} | Made using repl.it | Playing uthelp'.format(self.bot.user.id, user))
        sended=await ctx.send(embed=embed)
        await sended.add_reaction(emoji='\U0001f44d')
        await sended.add_reaction(emoji='\U0001f44e')
        await sended.add_reaction(emoji='\U00002699')
    @commands.command(
        name='serverinfo',
        description='View server info.',
        aliases=['server', 'guild']
    )
    async def someother(self, ctx):
        humans=0
        bots=0
        for member in ctx.guild.members:
            if member.bot:
                bots+=1
            else:
                humans+=1
        online=0
        offline=0
        dnd=0
        idle=0
        for member in ctx.guild.members:
            if member.status == discord.Status.online:
                online += 1
            elif member.status == discord.Status.offline:
                offline += 1
            elif member.status == discord.Status.dnd:
                dnd += 1
            elif member.status == discord.Status.idle:
                idle += 1
        embed=discord.Embed(title='__{}__'.format(ctx.guild), color=0x000000)
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.add_field(name='__General:__', value='**ID:** {}\n**Created:** {} (UTC)\n**Owner:** {}\n**Roles:** {}'.format(ctx.guild.id, ctx.guild.created_at, ctx.guild.owner, len(ctx.guild.roles)), inline=False)
        embed.add_field(name='__Members__', value='**Members:** {}\n**Humans:** {}\n**Bots:** {}'.format(len(ctx.guild.members), humans, bots), inline=True)
        embed.add_field(name='__Online__', value='**Online:** {}\n**Offline:** {}\n**Dnd:** {}\n**Idle:** {}'.format(online, offline, dnd, idle), inline=True)
        embed.add_field(name='__Channels__', value='**Text:** {}\n**Voice:** {}'.format(len(ctx.guild.text_channels), len(ctx.guild.voice_channels)), inline=False)
        embed.add_field(name='__Max members__:', value='{}'.format(ctx.guild.max_members), inline=False)
        embed.add_field(name='__Region:__', value='{}'.format(ctx.guild.region), inline=False)
        embed.add_field(name='__Description:__', value='{}'.format(ctx.guild.description), inline=False)
        await ctx.send(embed=embed)

    @commands.command(
        name='source',
        description='View bot src.',
        aliases=['src']
    )
    async def send_link(self, ctx):
        await ctx.send('https://github.com/insert-ctrl/discord-utils-src')

    @commands.command(
        name='prefixes',
        description='Get all prefixes.',
        aliases=[]
    )
    async def send_prefixes(self, ctx):
        prefixes = ['ut.', '[[']
        await ctx.send('**discord utils prefixes**\n{}'.format(prefixes))

    @commands.command(
        name='about',
        description='View bot description.',
        aliases=['__a__']
    )
    async def about(self, ctx):
        owner = self.bot.get_user(self.bot.owner_id)
        embed=discord.Embed(title='About thel vadam likes nothing jr', color=0x000000)
        embed.add_field(name='Purpose:', value='thel vadam likes nothing jr\'s purpose is to be fun discord bot with some basic utility purposes such as kick, ban, etc. He also has some fun/misc features such as getting the binary code for whatever number or char, same with ascii. (tho the unicode part isnt working). thel vadam likes nothing jr is still in beta, so there are probably some bugs. DM his owner if you find any bugs.\nPlaying ut._help for help.', inline=False)
        embed.set_footer(text='Made by {}'.format(owner))
        await ctx.send(embed=embed)

    @commands.command(
        name='help'
    )
    async def _help_(self, ctx, comm='all'):
        if comm == 'all':
            embed=discord.Embed(title='thel vadam likes nothing jr.\'s help page', description='Use `ut.help [command]` for info on command, or `ut.module [module name]` for help on specific module.', color=0x000000)
            cogs = [c for c in self.bot.cogs.keys()]
            for cog in cogs:
            # Get a list of all commands under each cog

                cog_commands = self.bot.get_cog(cog).get_commands()
                commands_list = ''
                for comm in cog_commands:
                    commands_list += f'`{comm.name}` '

                # Add the cog's details to the embed.

                embed.add_field(
                    name=cog,
                    value=commands_list,
                    inline=False
                )
            await ctx.send(embed=embed)
        else:
            cogs = [c for c in self.bot.cogs.keys()]
            for cog in cogs:
                commands_list = self.bot.get_cog(cog).get_commands()
                for comm_ in commands_list:
                    if comm_.name == comm:
                        embed=discord.Embed(title='`{}`'.format(comm_.name), description='{}'.format(comm_.description), color=0x000000)
                        if len(comm_.aliases) > 0:
                            embed.add_field(name='Aliases', value='`{}`'.format('|'.join(comm_.aliases)), inline=False)
                        await ctx.send(embed=embed)
                        return
            await ctx.send('Command not found.')
    
    @commands.command(
        name='module',
        description='View module info (on module oc)',
        aliases=['cog']
    )
    async def _cogs(self, ctx, module='all'):
        cogs = [c for c in self.bot.cogs.keys()]
        if module == 'all':
            embed=discord.Embed(
                title='',
                color=0x000000
            )
            all_ = ''
            for cog in cogs:
                all_ += '`{}`\n'.format(cog)
            embed.add_field(
                name='Modules:',
                value=all_
            )
            await ctx.send(embed=embed)
            
        else:
            if module in cogs:
                embed=discord.Embed(title=module, color=0x000000)
                comm_list = self.bot.get_cog(cogs[cogs.index(module)]).get_commands()
                

                text = '```'

                for comm in comm_list:
                    text += '{}\n'.format(comm)
                text += '```'
                embed.add_field(name='Commands:',value=text, inline=False)
                await ctx.send(embed=embed)
                return
            await ctx.send('Module not found. Remember: module names are case sensitive.')



        






    



def setup(bot):
    bot.add_cog(Stuff(bot))

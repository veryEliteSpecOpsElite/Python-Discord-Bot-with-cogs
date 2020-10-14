from discord.ext import commands
from keep_alive import keep_alive
from discord.utils import get
import discord, os
from dotenv import load_dotenv
import jishaku

def pow_(base, power):
    return 

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

start=0

def get_prefix(client, message):

    prefixes = ['ut.', 'ut', 'ut,']   

    if not message.guild:
        prefixes = ['ut.']   
    return commands.when_mentioned_or(*prefixes)(client, message)


bot = commands.Bot(                         
    command_prefix=get_prefix,              
    description='A sorta useless Util bot.',  
    owner_id=640203987437748246,            
    case_insensitive=True             
)

cogs = ['cogs.basic', 'cogs.b_info', 'cogs.invite', 'cogs.roles', 'cogs.misc', 'cogs.tags', 'cogs.mod', 'cogs.gb', 'cogs.eval', 'cogs.owner_only', 'cogs.code']


@bot.event
async def on_ready():                                       
    print(f'Logged in as {bot.user.name} id:{bot.user.id}')
    bot.remove_command('help')
    for cog in cogs:
        bot.load_extension(cog)
        print(cog)
    bot.load_extension("jishaku")
    game=discord.Game('ut.help for help (duh)')
    await bot.change_presence(status=discord.Status.online, activity=game)
    return







keep_alive()
bot.run(token, bot=True, reconnect=True)

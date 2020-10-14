from discord.ext import commands

class Invite(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.command(
        name='invite',
        description='Send invite link',
        aliases=['inv']
    )
    async def send_li(self, ctx):
        await ctx.send('Invite link:\nhttps://discordapp.com/api/oauth2/authorize?client_id=665674407611727915&permissions=8&scope=bot')


def setup(bot):
    bot.add_cog(Invite(bot)) 

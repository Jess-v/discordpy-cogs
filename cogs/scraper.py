import discord
from discord.ext import commands

message_log = "msg_scrape.txt"
max_limit = 10000


class Scrape(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def scrape(self, ctx: commands.Context, user: discord.Member = None):
        if user is None:
            await ctx.send('Please tag a user who\'s messages are to be scraped.')
        else:
            await ctx.send(f'Beginning to scrape messages of {user.display_name} in channel {ctx.channel.name}')
            log = open(message_log, 'a', encoding='utf-8')
            async for message in ctx.channel.history(limit=max_limit):
                if message.author == user:
                    log.write(f'<|startoftext|>\n{message.content}\n<|endoftext|>\n\n')
            await ctx.send(f'Scrape complete!')


def setup(bot):
    bot.add_cog(Scrape(bot))

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
            for guild in self.bot.guilds:
                await ctx.send(f'Beginning to scrape messages of {user.display_name} in server {guild.name}')
                for channel in guild.text_channels:
                    await ctx.send(f'Beginning to scrape messages of {user.display_name} in channel {channel.name}')
                    log = open(message_log, 'a', encoding='utf-8')
                    try:
                        async for message in channel.history(limit=max_limit):
                            if message.author == user:
                                log.write(f'<|startoftext|>\n{message.content}\n<|endoftext|>\n\n')
                    except:
                        await ctx.send('Permission error scraping this channel.')
                    await ctx.send(f'Scrape complete!')


def setup(bot):
    bot.add_cog(Scrape(bot))


from discord.ext import commands
import time
import random


class Dice(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def roll(self, ctx: commands.Context, arg: str = '1d20'):

        roll_args = arg.split('d')
        to_add = 0

        random.seed(time.time() * random.random())

        if len(roll_args) != 2:
            await ctx.send('Invalid command syntax. Your roll should look something like 1d20+1')

        if '+' in roll_args[1] or '-' in roll_args[1]:
            to_mod = roll_args.pop(1)
            if '+' in to_mod:
                to_mod = to_mod.split('+')

                roll_args.extend(to_mod)

                to_add = int(roll_args[2])
            else:
                to_mod = to_mod.split('-')

                roll_args.extend(to_mod)

                to_add = -1 * int(roll_args[2])

        result = 0
        l_index = 0

        while l_index < int(roll_args[0]):
            result += random.randint(1, int(roll_args[1]))
            l_index += 1

        result += to_add

        await ctx.send(f'Result: {result}')

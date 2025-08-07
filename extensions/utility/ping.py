from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"{self.bot.user.name} hits {ctx.author.mention} with an Axe! and it only took {self.bot.latency * 1000:.0f} ms to hit you!")

async def setup(bot):
    await bot.add_cog(Ping(bot))
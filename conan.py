import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

intents = discord.Intents.default()
intents.members = True
intents.message_content = True


class Conan(commands.Bot):
    """A simple Discord bot structure."""

    def __init__(self):
        super().__init__(
            command_prefix="!", description="barebones bot structure", intents=intents
        )

    async def on_ready(self):
        print(f"{self.user.name} is online!")

    async def setup_hook(self):
        @self.command()
        async def ping(ctx):
            await ctx.send(f"{self.user.name} hits {ctx.author.mention} with an Axe!")

Conan().run(BOT_TOKEN)

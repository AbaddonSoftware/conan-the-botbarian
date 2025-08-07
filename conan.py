import os
import logging
from pathlib import Path
from dotenv import load_dotenv
import discord
from discord.ext import commands

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("conan")

BOT_TOKEN = os.environ.get("BOT_TOKEN")
# is_docker = True
is_docker = os.environ.get("is_docker")
if not is_docker:
    load_dotenv()
    BOT_TOKEN = os.environ.get("BOT_TOKEN")

    




intents = discord.Intents.default()
intents.members = True
intents.message_content = True

extensions = ["extensions.utility.ping"]

class Conan(commands.Bot):
    """A barebones discord bot structure."""

    def __init__(self):
        super().__init__(
            command_prefix="!", description="A barebones discord bot structure", intents=intents
        )

    async def on_ready(self):
        print(f"{self.user.name} is online!")

    async def setup_hook(self):
        for extension in extensions:
            await self.load_extension(extension)

Conan().run(BOT_TOKEN)

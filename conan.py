import os
import logging
from pathlib import Path
import discord
from discord.ext import commands

running_in_docker = Path("/.dockerenv").exists()
if not running_in_docker:
    from dotenv import load_dotenv

    load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("conan")



BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN is not set")

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

extensions = ["extensions.utility.ping"]


class Conan(commands.Bot):
    """A barebones discord bot structure."""

    def __init__(self):
        super().__init__(
            command_prefix="!",
            description="A barebones discord bot structure",
            intents=intents,
        )

    async def on_ready(self):
        print(f"{self.user.name} is online!")

    async def setup_hook(self):
        for extension in extensions:
            await self.load_extension(extension)


Conan().run(BOT_TOKEN)

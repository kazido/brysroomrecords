from pydis_core import BotBase
from logging import getLogger

from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie

from utils import logs

log = getLogger("bot")


class StartupError(Exception):
    """Exception class for startup errors."""

    def __init__(self, base: Exception):
        super().__init__()
        self.exception = base


class Bot(BotBase):
    async def setup_hook(self) -> None:
        await super().setup_hook()

        # Logging setup
        logs.setup()

        # Database setup
        client = AsyncIOMotorClient(URI)
        await init_beanie(database=client.discordbot, document_models=[MK8DXRecords])

        # Load our own extensions using function from discord.py's own bot
        await self.load_extensions(exts)

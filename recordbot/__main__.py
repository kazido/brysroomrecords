import asyncio
import discord
import os
import argparse
import recordbot

from discord.ext import commands
from pydis_core import StartupError
from cococap.bot import Bot
from logging import getLogger

log = getLogger(__name__)


async def main():
    # discord bot permissions
    intents = discord.Intents.all()
    intents.message_content = True
    intents.presences = False
    intents.dm_typing = False
    intents.dm_reactions = False
    intents.invites = False
    intents.webhooks = False
    intents.integrations = False

    recordbot.instance = Bot(
        guild_id=856915776345866240,
        command_prefix=commands.when_mentioned_or("."),
        activity=discord.Game(name=f"Upload your records!"),
        case_insensitive=True,
        max_messages=10_000,
        allowed_mentions=discord.AllowedMentions(everyone=False),
        intents=intents,
        strip_after_prefix=True,
        allowed_roles=None,
        http_session=None,
    )

    async with recordbot.instance as _bot:
        await _bot.start(recordbot.TOKEN, reconnect=True)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except StartupError as e:
        message = "Unknown Startup Error Occurred."
    except KeyboardInterrupt:
        log.critical("Bot shutting down due to manual interrupt.")

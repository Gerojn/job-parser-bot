from aiogram import Bot, Dispatcher

from app.config import BOT_TOKEN
from app.handlers.common import router


def create_dispatcher() -> Dispatcher:
    dp = Dispatcher()
    dp.include_router(router)
    return dp


def create_bot() -> Bot:
    return Bot(token=BOT_TOKEN)
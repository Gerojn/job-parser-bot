import asyncio

from app.bot import create_bot, create_dispatcher


async def main() -> None:
    print("Starting bot...")
    bot = create_bot()
    dp = create_dispatcher()
    print("Polling started")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
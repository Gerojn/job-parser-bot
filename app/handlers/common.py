from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from app.keyboards.main import main_keyboard
from app.services.jobs import get_mock_jobs


router = Router()


@router.message(CommandStart())
async def start_handler(message: Message) -> None:
    await message.answer(
        text=(
            "Привіт!\n"
            "Я бот для пошуку вакансій.\n"
            "Натисни кнопку нижче, щоб подивитися вакансії."
        ),
        reply_markup=main_keyboard,
    )


@router.message(lambda message: message.text == "Показати вакансії")
async def show_jobs_handler(message: Message) -> None:
    jobs = get_mock_jobs()

    if not jobs:
        await message.answer("Вакансій зараз немає.")
        return

    lines = []

    for job in jobs:
        lines.append(
            f"📌 {job['title']}\n"
            f"Компанія: {job['company']}\n"
            f"Локація: {job['location']}\n"
            f"Посилання: {job['url']}"
        )

    response_text = "\n\n".join(lines)
    await message.answer(response_text)
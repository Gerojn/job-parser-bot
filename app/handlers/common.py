from aiogram import Router, F
from aiogram.filters import Command, CommandStart
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
            "Натисни кнопку нижче, щоб подивитися список вакансій.\n\n"
            "Також доступна команда /help."
        ),
        reply_markup=main_keyboard,
    )


@router.message(Command("help"))
async def help_handler(message: Message) -> None:
    await message.answer(
        text=(
            "Доступні команди:\n"
            "/start — запуск бота\n"
            "/help — показати допомогу\n\n"
            "Або натисни кнопку 'Показати вакансії'."
        ),
        reply_markup=main_keyboard,
    )


@router.message(F.text == "Показати вакансії")
async def show_jobs_handler(message: Message) -> None:
    jobs = get_mock_jobs()

    if not jobs:
        await message.answer("Вакансій зараз немає.")
        return

    lines = []

    for index, job in enumerate(jobs, start=1):
        lines.append(
            f"{index}. 📌 {job['title']}\n"
            f"Компанія: {job['company']}\n"
            f"Локація: {job['location']}\n"
            f"Посилання: {job['url']}"
        )

    response_text = "Ось актуальний список вакансій:\n\n" + "\n\n".join(lines)
    await message.answer(response_text)
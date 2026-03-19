from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram import Router

router = Router()


@router.message(CommandStart())
async def handle_start(message: Message) -> None:
    await message.answer("✅ Бот запущен и готов работать.")

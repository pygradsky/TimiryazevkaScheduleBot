from aiogram.filters import CommandStart
from aiogram import Router, types

from src.db.db_operations import save_user_info
from src.bot.resources.messages import bot_messages

router = Router()


@router.message(CommandStart())
async def handle_start(message: types.Message) -> None:
    await save_user_info(message.from_user.id, message.from_user.username)
    await message.answer(
        bot_messages['/start']
    )

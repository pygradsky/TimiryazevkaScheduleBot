from aiogram import Router, types
from aiogram.filters import Command

from src.db.db_operations import get_user_info
from src.bot.resources.messages import bot_messages

router = Router()


@router.message(Command('clock'))
async def handle_clock(message: types.Message):
    user_info = await get_user_info(message.from_user.id)
    if not user_info:
        await message.answer(
            bot_messages['no_user_info']
        )
        return
    await message.answer(
        bot_messages['/clock']
    )

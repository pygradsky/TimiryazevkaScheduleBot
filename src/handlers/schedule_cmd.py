from aiogram import Router, types
from aiogram.enums import ParseMode
from aiogram.filters import Command

from src.db.db_operations import get_user_info

router = Router()


@router.message(Command('schedule'))
async def handle_clock(message: types.Message):
    user_info = await get_user_info(message.from_user.id)
    if not user_info:
        await message.answer(
            '⚠️ Не смогли обработать ваши данные. <b>Пройдите регистрацию</b> и попробуйте ещё раз.',
            parse_mode=ParseMode.HTML,
        )
        return
    await message.answer(
        '⌛ Получаю список расписаний. Это может занять некоторое время...'
    )

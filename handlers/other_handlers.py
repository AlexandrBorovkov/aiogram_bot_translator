from aiogram import Router
from aiogram.types import Message
from lexicon.lexicon_ru import TEXT


router = Router()

@router.message()
async def send_answer(message: Message):
    await message.answer(text=TEXT['other_answer'])
    
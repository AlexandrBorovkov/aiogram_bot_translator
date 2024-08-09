from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


from lexicon.lexicon_ru import TEXT


button_en_ru = KeyboardButton(text=TEXT['en_ru'])
button_ru_en = KeyboardButton(text=TEXT['ru_en'])

settings_kb = ReplyKeyboardMarkup(
    keyboard=[[button_en_ru],
              [button_ru_en]],
              resize_keyboard=True)




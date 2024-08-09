from aiogram import F, Router
from aiogram.filters import Command, CommandStart, StateFilter   
from aiogram.types import Message
from aiogram.fsm.context import FSMContext                       
from aiogram.fsm.state import State, StatesGroup  
from aiogram.fsm.storage.memory import MemoryStorage    
from aiogram.types import ReplyKeyboardRemove          
from keyboards.keyboards import settings_kb
from lexicon.lexicon_ru import TEXT
from services.services import translation_func


router = Router()

storage = MemoryStorage()                                    

class Form(StatesGroup):                                     
    language = State()                                       
    input_text = State()                                           
                                        

@router.message(CommandStart())      
async def process_start(message: Message, state: FSMContext):    
    await message.answer(text=TEXT['/start'], reply_markup=settings_kb)
    await state.set_state(Form.language)                         

@router.message(Command(commands='help'))  
async def process_help(message: Message):
    await message.answer(text=TEXT['/help'])

@router.message(Command(commands='change_the_language'))  
async def process_change(message: Message, state: FSMContext):
    await message.answer(text=TEXT['/change_the_language'], reply_markup=settings_kb)
    await state.set_state(Form.language)

@router.message(StateFilter(Form.language), (F.text == TEXT['en_ru']) | (F.text == TEXT['ru_en']))    
async def but_en_ru(message: Message, state: FSMContext): 

    if message.text == TEXT['en_ru']:
        language = 'en'
        await message.answer(TEXT['input_text_eng'], reply_markup=ReplyKeyboardRemove())
    else:
        language = 'ru'
        await message.answer(TEXT['input_text_rus'], reply_markup=ReplyKeyboardRemove())

    await state.update_data(language=language) 

    

    await state.set_state(Form.input_text)                         


@router.message(StateFilter(Form.input_text))
async def translat(message: Message, state: FSMContext):    
    user_data = await state.get_data()
    language = user_data.get('language')

    result = await translation_func(language, message.text)

    await message.answer(result)
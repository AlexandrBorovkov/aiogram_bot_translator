from aiogram import Bot
from aiogram.types import BotCommand

async def set_main_menu(bot: Bot):

    main_menu_commands = [
        BotCommand(command='/start',
                   description='Старт'),
        BotCommand(command='/help',
                   description='Справка по работе бота'),
        BotCommand(command='/change_the_language',
                   description='Сменить язык ввода')  
    ]

    await bot.set_my_commands(main_menu_commands)
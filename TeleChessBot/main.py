import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import app.keyboards as kb

bot = Bot(token='7220836560:AAGfQ0PFrAy-OVE7vqhlsfJEeh1i5fJ2mes')
dp = Dispatcher()
m = 0

class check():
    m = 0

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет, этот бот предложит тебе несколько задач по шахматам!', reply_markup=kb.main)

@dp.message(F.text == 'Назад')
async def cmd_start(message: Message):
    await message.answer('Привет, этот бот предложит тебе несколько задач по шахматам!', reply_markup=kb.main)

@dp.message(F.text == 'Мат в 1 ход')
async def mat1(message: Message, state: FSMContext):
    check.m = 1
    await message.answer('Поставьте сопернику мат в один код!', reply_markup=kb.rep)
    await message.answer_photo(photo='AgACAgIAAxkBAAMHZ2sKUBkFc6B9Tu9Rm1KrwXw8imQAAhroMRuZzWBLTg7xfiNgfMUBAAMCAAN4AAM2BA')


@dp.message(F.text == 'Мат в 2 хода')
async def mat1(message: Message, state: FSMContext):
    check.m = 2
    await message.answer('Поставьте сопернику мат в два кода!', reply_markup=kb.rep)
    await message.answer_photo(photo='AgACAgIAAxkBAAMJZ2sKb7d7kGdhRgTksoR2nb7rB54AAh_oMRuZzWBLcYxoIJU1x7YBAAMCAAN4AAM2BA')

@dp.message(F.text == 'Мат в 4 хода')
async def mat1(message: Message):
    check.m = 3
    await message.answer('Поставьте сопернику мат в четыре кода!', reply_markup=kb.rep)
    await message.answer_photo(photo='AgACAgIAAxkBAAMLZ2sKebLew7whKOwo0Z5Yy67PwfEAAiHoMRuZzWBLBBfwK2L2ilgBAAMCAAN4AAM2BA')

@dp.message(F.text == 'Наименования фигур')
async def mat1(message: Message):
    await message.answer('Изучите наименования фигур!')
    await message.answer_photo(photo='AgACAgIAAxkBAAMfZ2sXyqW_9Le0K-yX3srcmRlSEaMAAo3oMRuZzWBLyAGBCSLAa7kBAAMCAAN5AAM2BA', reply_markup=kb.back)

@dp.message(F.text == 'Показать ответ')
async def mat1(message: Message):
    if check.m == 1:
        await message.answer(text= 'qg4')
    if check.m == 2:
        await message.answer(text= 'qa6 qb7')
    if check.m == 3:
        await message.answer(text= 'qf6 rg3 qh6 qd6')

@dp.message()
async def send_example(message: Message):
    if check.m != 0:
        if (message.text == 'qg4' and check.m == 1) or (message.text == 'qa6 qb7' and check.m == 2) or ((message.text == 'qf6 rg3 qh6 qd6' and check.m == 3)):
            await message.answer(text='Молодец!', reply_markup=kb.rep)
            check.m = 0
        else:
            await message.answer(text='Неверно, попробуй еще раз')

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')



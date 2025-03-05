from aiogram import Router, types, F, Bot
from aiogram.filters import CommandStart, Command, or_f


from kbds.inline import MenuCallBack, get_user_prices_btns, get_user_prices_price_btns
from utils.parsing_crypto import get_price

from filters.chat_type import ChatTypeFilter

from kbds.reply import get_keyboard, del_kb

from handlers.menu_processing import get_menu_content

from database.models import User
from sqlalchemy import select

from sqlalchemy.ext.asyncio import AsyncSession

user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(["private"]))

@user_private_router.message(CommandStart())
async def start_cmd_handler(message: types.Message, session: AsyncSession):
    description, reply_markup = await get_menu_content(session, level=0, menu_name="main")
    
    await message.answer(description, reply_markup=reply_markup)
    
@user_private_router.callback_query(MenuCallBack.filter())
async def user_menu(callback: types.CallbackQuery, callback_data: MenuCallBack, session: AsyncSession):
    description, reply_markup = await get_menu_content(
        session,
        level=callback_data.level,
        menu_name=callback_data.menu_name
    )
    await callback.message.edit_text(description, reply_markup=reply_markup)
    await callback.answer()
    
@user_private_router.callback_query(F.data.startswith("prices"))
async def show_prices_menu(callback: types.CallbackQuery, session: AsyncSession):
    """Обработчик кнопки 'Курсы криптовалют 🪙'"""
    reply_markup = get_user_prices_btns(level=2)
    
    await callback.message.edit_text("Выберите криптовалюту:", reply_markup=reply_markup)
    await callback.answer()

@user_private_router.callback_query(F.data.startswith("usdt_btc"))
async def show_btc_price(callback: types.CallbackQuery, session: AsyncSession):
    """Обработчик кнопки 'BTCUSDT'"""
    # Здесь должен быть запрос к API Binance для получения цены BTC/USDT
    btc_price = get_price("BTCUSDT")

    reply_markup = get_user_prices_price_btns(level=3)
    
    await callback.message.edit_text(f"{btc_price}\n\nНажмите 'Назад' для возврата.", reply_markup=reply_markup)
    await callback.answer()

@user_private_router.callback_query(F.data.startswith("usdt_ton"))
async def show_ton_price(callback: types.CallbackQuery, session: AsyncSession):
    """Обработчик кнопки 'TONUSDT'"""
    # Здесь должен быть запрос к API Binance для получения цены TON/USDT
    ton_price = get_price("TONUSDT")  # Заглушка

    reply_markup = get_user_prices_price_btns(level=3)
    
    await callback.message.edit_text(f"{ton_price}\n\nНажмите 'Назад' для возврата.", reply_markup=reply_markup)
    await callback.answer()

@user_private_router.callback_query(F.data.startswith("back_to_prices"))
async def back_to_prices_menu(callback: types.CallbackQuery, session: AsyncSession):
    """Обработчик кнопки 'Назад 🔙' в меню цен"""
    reply_markup = get_user_prices_btns(level=2)
    
    await callback.message.edit_text("Выберите криптовалюту:", reply_markup=reply_markup)
    await callback.answer()

@user_private_router.message(Command("crypto"))
async def crypto_cmd_handler(message: types.Message, session: AsyncSession):
    user_id = message.from_user.id
    
    query = select(User).where(User.user_id == user_id)
    result = await session.execute(query)
    user = result.scalar_one_or_none()  # Возвращает None, если пользователя нет

    if user is None:
        await message.reply("Чтобы пользоваться услугами бота 🤖 \nОплатите подписку 💸 /subscribe")
    else:
        await message.answer(
            "Выберите валюту",
            reply_markup=get_keyboard(
                "/BTCUSDT",
                "/TONUSDT",
                placeholder="Выберите валюту",
                sizes=(1,)
            )
        )
        
@user_private_router.message(Command("BTCUSDT"))
async def get_price_btc_handler(message: types.Message):
    price = get_price("BTCUSDT")
    
    if price is not None:
        await message.answer(f"Цена BTC: {price} USDT", reply_markup=del_kb)
    else:
        await message.answer("Не удалось получить цену.")

@user_private_router.message(Command("TONUSDT"))
async def get_price_btc_handler(message: types.Message):
    price = get_price("TONUSDT")
    
    if price is not None:
        await message.answer(f"Цена TON: {price} USDT", reply_markup=del_kb)
    else:
        await message.answer("Не удалось получить цену.")
        


        

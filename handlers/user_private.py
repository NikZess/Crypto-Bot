from aiogram import Router, types, F, Bot
from aiogram.filters import CommandStart, Command, or_f


from kbds.inline import MenuCallBack, get_user_prices_btns
from utils.parsing_crypto import get_price

from filters.chat_type import ChatTypeFilter

from kbds.reply import get_keyboard, del_kb
from kbds.inline import get_prices_keyboard

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
            text="<strong>Доступные валюты</strong>",
            reply_markup=get_prices_keyboard()
        )
        
@user_private_router.callback_query(F.data.startswith("usdt"))
async def get_price_usdt(callback_query: types.CallbackQuery) -> None:
    data = callback_query.data
    result = data.split("_")[1]
    print(result)
    
    if result == "btc":
        price_crypto = get_price("BTCUSDT")
        await callback_query.message.answer(f"Цена BTC: {price_crypto}")
          
    if result == "ton":
        price_crypto = get_price("TONUSDT")
        await callback_query.message.answer(f"Цена TON: {price_crypto}")


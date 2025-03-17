import os

from aiogram import Router, types, F, Bot
from aiogram.filters import CommandStart, Command

from kbds.inline import MenuCallBack

from APIparsers.currency_market.binanceAPI_parsing import get_price

from filters.chat_type import ChatTypeFilter

from kbds.inline import get_prices_keyboard
from kbds.reply import del_kb

from handlers.menu_processing import get_menu_content

from database.models import User
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(["private"]))

@user_private_router.message(CommandStart())
async def start_cmd_handler(message: types.Message, session: AsyncSession):
    description, reply_markup = await get_menu_content(session, level=0, menu_name="main", message=message)
    
    await message.answer(description, reply_markup=reply_markup)

@user_private_router.callback_query(MenuCallBack.filter())
async def user_menu(callback: types.CallbackQuery, callback_data: MenuCallBack, session: AsyncSession):
    description, reply_markup = await get_menu_content(
        session,
        level=callback_data.level,
        menu_name=callback_data.menu_name,
        message=callback.message
    )
    
    try:
        await callback.message.edit_text(description, reply_markup=reply_markup)
    except Exception as e:
        await callback.answer("Не удалось обновить меню. Попробуйте позже.")

    await callback.answer()

@user_private_router.message(Command("crypto"))
async def crypto_cmd_handler(message: types.Message, session: AsyncSession):
    user_id = message.from_user.id
    
    query = select(User).where(User.user_id == user_id)
    result = await session.execute(query)
    user = result.scalar_one_or_none()  

    if user is None:
        await message.reply("Чтобы пользоваться услугами бота 🤖 \nОплатите подписку 💸 /subscribe")
    else:
        await message.answer(
            text="<strong>Доступные валюты</strong>",
            reply_markup=get_prices_keyboard()
        )

@user_private_router.callback_query(F.data.startswith("usdt"))
async def get_price_usdt(callback_query: types.CallbackQuery):
    data = callback_query.data
    currency = data.split("_")[1].upper()
    
    price = await get_price(f"{currency}USDT")
    await callback_query.message.answer(f"Цена {currency} в USDT: {price}")

@user_private_router.callback_query(F.data.startswith("currency"))
async def user_settings_currency_handler(callback_query: types.CallbackQuery, session: AsyncSession):
    data = callback_query.data
    user_set_currency = data.split('_')[-1].upper()
    
    # Обновляем валюту в базе данных
    user_id = callback_query.from_user.id
    query = select(User).where(User.user_id == user_id)
    result = await session.execute(query)
    user = result.scalar_one_or_none()

    if user:
        user.currency = user_set_currency  
        await session.commit()
        await callback_query.answer(f"Валюта изменена на {user_set_currency}")
    else:
        await callback_query.answer("Ошибка: пользователь не найден")

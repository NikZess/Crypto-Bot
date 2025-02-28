from aiogram import Router, types, F, Bot
from aiogram.filters import CommandStart, Command, or_f
from aiogram.types import LabeledPrice, PreCheckoutQuery, Message

from utils.parsing_crypto import get_price

from filters.chat_type import ChatTypeFilter

from kbds.reply import get_keyboard, del_kb

from database.models import User
from sqlalchemy import select

from sqlalchemy.ext.asyncio import AsyncSession


user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(["private"]))

@user_private_router.message(CommandStart())
async def start_cmd_handler(message: types.Message):
    await message.answer("🖐️Привет! Это крипто бот, который поможет \nузнать курсы криптовалют на бирже Binance 💵")
    
@user_private_router.message(Command("crypto"))
async def crypto_cmd_handler(message: types.Message, session: AsyncSession):
    user_id = message.from_user.id
    
    query = select(User).where(User.user_id == user_id)
    result = await session.execute(query)
    user = result.scalar_one_or_none()  # Возвращает None, если пользователя нет

    if user is None:
        await message.reply("Чтобы пользоваться услугами бота 🤖 \nОплатите подписку 💸")
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
        


        

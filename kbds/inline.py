from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData

class MenuCallBack(CallbackData, prefix="menu"):
    level: float
    menu_name: str
    page: int = 0

def get_purchase_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="1 месяц 💸", callback_data="buy_1")],
        [InlineKeyboardButton(text="3 месяца 🤑", callback_data="buy_2")],
        [InlineKeyboardButton(text="1 год 💰", callback_data="buy_3")],
    ])

def get_prices_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="BTC", callback_data="usdt_btc")],
        [InlineKeyboardButton(text="TON", callback_data="usdt_ton")],
        [InlineKeyboardButton(text="ETH", callback_data="usdt_eth")],
        [InlineKeyboardButton(text="XRP", callback_data="usdt_xrp")],
        [InlineKeyboardButton(text="DOGE", callback_data="usdt_doge")],
    ])
    
# |* \\\ Работа с главным меню \\\ *|    
    
def get_user_main_btns(*, level: float, sizes: tuple[int] = (2, 1, 1)) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()
    
    btns = {
        "Курсы криптовалют 🪙": "prices",
        "О нас ℹ️": "about",
        "Настройки ⚙️": "settings",
    }
    
    for text, menu_name in btns.items():
        if menu_name == "prices":
            keyboard.add(InlineKeyboardButton(
                text=text,
                callback_data=MenuCallBack(level=1.0, menu_name=menu_name).pack()
            ))
        
        if menu_name == "about":
            keyboard.add(InlineKeyboardButton(
                text=text,
                callback_data=MenuCallBack(level=2.0, menu_name=menu_name).pack()
            ))
        
        if menu_name == "settings":
            keyboard.add(InlineKeyboardButton(
                text=text,
                callback_data=MenuCallBack(level=3.0, menu_name=menu_name).pack()
            ))
        
    return keyboard.adjust(*sizes).as_markup()

# |* \\\ Работа с меню информации об функции /price \\\ *|

def get_user_prices_btns(*, level: float, sizes: tuple[int] = (1, )) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()
    
    btns = {
        "Назад 🔙": "back_menu_from_prices",
    }
    
    for text, menu_name in btns.items():
        if menu_name == "back_menu_from_prices":
            keyboard.add(InlineKeyboardButton(
                text=text,
                callback_data=MenuCallBack(level=0, menu_name="main").pack()
            ))

    return keyboard.adjust(*sizes).as_markup()

# |* \\\ Работа с меню информации о боте и о др. \\\ *|

def get_user_about_btns(*, level: float, sizes: tuple[int] = (1,)) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()
    
    btns = {
        "Поддержать нас": "donate",
        "Назад 🔙": "back_menu_from_about",
    }
    
    for text, menu_name in btns.items():
        if menu_name == "donate":
            keyboard.add(InlineKeyboardButton(
                text=text,
                callback_data=MenuCallBack(level=2.1, menu_name=menu_name).pack()
            ))
        
        elif menu_name == "back_menu_from_about":
            keyboard.add(InlineKeyboardButton(
                text=text,
                callback_data=MenuCallBack(level=0, menu_name="main").pack()
            ))
        
    return keyboard.adjust(*sizes).as_markup()

# |* \\\ Работа с меню настроек \\\ *|

def get_user_settings_btns(*, level: float, sizes: tuple[int] = (1,)) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()

    btns = {
        "Биржи 💲": "market",
        "Валюта показа 💱": "currency",
        "Язык бота (скоро) 🏳": "language",
        "Назад 🔙": "back_menu_from_settings",
    }

    for text, menu_name in btns.items():
        if menu_name == "market":
            keyboard.add(InlineKeyboardButton(
                text=text,
                callback_data=MenuCallBack(level=3.1, menu_name=menu_name).pack()
            ))
        
        if menu_name == "currency":
            keyboard.add(InlineKeyboardButton(
                text=text,
                callback_data=MenuCallBack(level=3.2, menu_name=menu_name).pack()
            ))
        
        if menu_name == "language":
            keyboard.add(InlineKeyboardButton(
                text=text,
                callback_data=MenuCallBack(level=3.3, menu_name=menu_name).pack()
            ))
        
        if menu_name == "back_menu_from_settings":
            keyboard.add(InlineKeyboardButton(
                text=text,
                callback_data=MenuCallBack(level=0, menu_name="main").pack()
            ))

    return keyboard.adjust(*sizes).as_markup()

def get_user_settings_market_btns(*, level: float, sizes: tuple[int] = (2,)) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()
    
    btns = {
        "ByBit": "stock_market_bybit",
        "Binance": "stock_market_binance",
        "BingX": "stock_market_bingx",
        "OKX": "stock_market_okx",
        "Назад 🔙": "back_menu_from_settings_market",
    }
    
    for text, menu_name in btns.items():
        if menu_name in ("stock_market_bybit", "stock_market_binance", "stock_market_bingx", "stock_market_bingx", "stock_market_okx"):
            keyboard.add(InlineKeyboardButton(
                text=text,
                callback_data=MenuCallBack(level=level, menu_name=menu_name).pack()
            ))
        
        if menu_name == "back_menu_from_settings_market":
            keyboard.add(InlineKeyboardButton(
                text=text,
                callback_data=MenuCallBack(level=3.0, menu_name=menu_name).pack()
            ))
    
    return keyboard.adjust(*sizes).as_markup()

def get_user_settings_currency_btns(*, level: float, sizes: tuple[int] = (2, 1)) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()
    
    btns = {
        "RUB": "currency_rub",
        "USDT": "currency_usdt",
        "EUR": "currency_eur",
        "Назад 🔙": "back_menu_from_settings_currency",
    }
    
    for text, menu_name in btns.items():
        if menu_name in ("currency_rub", "currency_usdt", "currency_eur"):
            keyboard.add(InlineKeyboardButton(
                text=text,
                callback_data=MenuCallBack(level=level, menu_name=menu_name).pack()
            ))
            
        if menu_name == "back_menu_from_settings_currency":
            keyboard.add(InlineKeyboardButton(
                text=text,
                callback_data=MenuCallBack(level=3.0, menu_name=menu_name).pack()
            ))
    
    return keyboard.adjust(*sizes).as_markup()

def get_user_settings_language_btns(*, level: float, sizes: tuple[int] = (2, 1)) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()
    
    btns = {
        "Русский / Russian": "language_russian",
        "Английский / English": "language_english",
        "Назад 🔙": "back_menu_from_settings_language",
    }
    
    for text, menu_name in btns.items():
        if menu_name in ("language_russian", "language_english"):
            keyboard.add(InlineKeyboardButton(
                text=text,
                callback_data=MenuCallBack(level=level, menu_name=menu_name).pack()
            ))
        
        if menu_name == "back_menu_from_settings_language":
            keyboard.add(InlineKeyboardButton(
                text=text,
                callback_data=MenuCallBack(level=3.0, menu_name=menu_name).pack()
            ))
            
    return keyboard.adjust(*sizes).as_markup()

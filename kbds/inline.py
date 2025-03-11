from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData

class MenuCallBack(CallbackData, prefix="menu"):
    level: int
    menu_name: str
    page: int = 1

def get_purchase_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="1 месяц 💸", callback_data="buy_1")],
        [InlineKeyboardButton(text="3 месяца 🤑", callback_data="buy_2")],
        [InlineKeyboardButton(text="1 год 💰", callback_data="buy_3")],
    ])

def get_prices_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="BTC", callback_data="usdt_btc")],
        [InlineKeyboardButton(text="TON", callback_data="usdt_ton")]
    ])
    
def get_user_main_btns(*, level: int, sizes: tuple[int] = (2, 1, 1)) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()
    
    btns = {
        "Курсы криптовалют 🪙": "prices",
        "О нас ℹ️": "about",
        "Настройки ⚙️": "settings",
        "Подписка 💸": "buy_subscribe"
    }
    
    for text, menu_name in btns.items():
        if menu_name == "prices":
            keyboard.add(InlineKeyboardButton(
                    text=text, 
                    callback_data=MenuCallBack(level=1, menu_name=menu_name).pack()
                ))
            
        elif menu_name == "about":
            keyboard.add(InlineKeyboardButton(
                    text=text,
                    callback_data=MenuCallBack(level=2, menu_name=menu_name).pack()
                ))
            
        elif menu_name == "settings":
            keyboard.add(InlineKeyboardButton(
                    text=text,
                    callback_data=MenuCallBack(level=3, menu_name=menu_name).pack()
                ))
        
        elif menu_name == "buy_subscribe":
            keyboard.add(InlineKeyboardButton(
                    text=text,
                    callback_data=MenuCallBack(level=level, menu_name=menu_name).pack()
                ))
        
    return keyboard.adjust(*sizes).as_markup()

def get_user_prices_btns(*, level: int, sizes: tuple[int] = (1,)) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()
    
    btns = {
        "Назад 🔙": "back_menu_from_prices",
        "BTC": "usdt_btc",
        "TON": "usdt_ton",
    }
    
    for text, menu_name in btns.items():
        if menu_name == "back_menu_from_prices":
            keyboard.add(InlineKeyboardButton(
                text=text,
                callback_data=MenuCallBack(level=0, menu_name="main").pack()
            ))
        elif menu_name in ["usdt_btc", "usdt_ton"]:
            keyboard.add(InlineKeyboardButton(
                text=text,
                callback_data=MenuCallBack(level=level, menu_name=menu_name).pack()
            ))
    return keyboard.adjust(*sizes).as_markup()

def get_user_about_btns(*, level: int, sizes: tuple[int] = (1,)) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()
    
    btns = {
        "Поддержать нас": "help",
        "Назад 🔙": "back_menu_from_about",
    }
    
    for text, menu_name in btns.items():
        if menu_name == "help":
            keyboard.add(InlineKeyboardButton(
                text=text,
                callback_data=MenuCallBack(level=level, menu_name=menu_name).pack()
            ))
        elif menu_name == "back_menu_from_about":
            keyboard.add(InlineKeyboardButton(
                text=text,
                callback_data=MenuCallBack(level=0, menu_name="main").pack()
            ))
    
    return keyboard.adjust(*sizes).as_markup()
        
def get_user_settings_btns(*, level: int, sizes: tuple[int] = (1,)) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()

    btns = {
        "Биржи 💲": "market",
        "Язык бота (скоро) 🏳": "language",
        "Назад 🔙": "back_main_from_settings"
    }

    for text, menu_name in btns.items():
        if menu_name in ["market", "language"]:
            keyboard.add(InlineKeyboardButton(
                text=text,
                callback_data=MenuCallBack(level=level, menu_name=menu_name).pack()
            ))
        elif menu_name == "back_main_from_settings":
            keyboard.add(InlineKeyboardButton(
                text=text,
                callback_data=MenuCallBack(level=0, menu_name="main").pack()  # level=0 ведет в главное меню
            ))

    return keyboard.adjust(*sizes).as_markup()
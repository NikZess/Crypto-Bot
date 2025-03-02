from aiogram.utils.formatting import Bold, as_list, as_marked_section
from aiogram.enums import ParseMode

description_for_info_pages = {
    "main_menu": "Привет 🖐️! <strong>Это Крипто-Бот 🤖</strong>, который поможет вам узнать\
криптовалют с различных бирж 💲. \n\nБиржу с которой вы хотите получить информацию можно изменить в настройках ⚙️.\
\n\nВсю информацию о нас можете узнать ниже 😉",
    "settings": "<strong>Настройки бота</strong>\n\n\
В настройках вы сами можете выбрать биржу для бота: <strong>ByBit, Binance, BingX, OKX</strong>\n\n\
На рахных биржах могут быть разные курсы валют \nВ боте используются API всех доступных для выбора бирж\n\n\
В настройках языка бота можно сменить язык: Русский/Английский",
    "about_menu": "<strong>Информация о боте</strong>"
}
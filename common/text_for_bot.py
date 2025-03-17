from sqlalchemy.ext.asyncio import AsyncSession
from database.engine import session_maker
from database.orm_query import orm_get_user_currency

async def init_descriptions(user_id: int, language: str = "ru"):
    async with session_maker() as session:
        user_settings_currency = await orm_get_user_currency(session, user_id=user_id) or "USD"  # Если None, ставим USD

    description_for_info_pages = {
        "ru": {
            "main_menu": "Привет 🖐️! <strong>Это Крипто-Бот 🤖</strong>, который поможет вам узнать курс "
                         "криптовалют с различных бирж 💲. \n\nБиржу с которой вы хотите получить информацию можно "
                         "изменить в настройках ⚙️.\n\nВсю информацию о нас можете узнать ниже 😉",

            "settings": "<strong>Настройки бота</strong>\n\n"
                        "В настройках вы сами можете выбрать биржу для бота: <strong>ByBit, Binance, BingX, OKX</strong>\n\n"
                        "На разных биржах могут быть разные курсы валют. В боте используются API всех доступных бирж.\n\n"
                        "В настройках языка можно сменить язык: Русский/Английский.",

            "about_menu": "<strong>Информация о боте</strong>\n\n"
                          "Разработчик данного крипто-бота - 1 человек. \n"
                          "Суть данного бота — отслеживать курсы валют с разных бирж и быть удобным.\n\n"
                          "Функции бота: \n\n"
                          "<strong>• Просмотр курсов валют \n"
                          "• Настройка биржи \n"
                          "• Настройка языка бота (в разработке) \n"
                          "• Алгоритм рекомендации покупки (в разработке)</strong>",

            "prices_menu": "<strong>Курсы валют</strong>",

            "settings_menu_currency": f"<strong>Меню настройки валюты бота</strong>\n\n"
                                       f"Выбранная валюта: {user_settings_currency}"
        },

        "en": {
            "main_menu": "Hi 🖐️! <strong>This is a Crypto Bot 🤖</strong>, that will help you find out the exchange rate of "
                         "cryptocurrencies from various exchanges 💲. \n\nYou can change the exchange in the settings ⚙️.\n\n"
                         "All information about us can be found below 😉",

            "settings": "<strong>Bot settings</strong>\n\n"
                        "You can choose the exchange for the bot: <strong>ByBit, Binance, BingX, OKX</strong>\n\n"
                        "There may be different exchange rates on these exchanges. The bot uses the APIs of all available exchanges.\n\n"
                        "You can change the language to Russian/English in the settings.",

            "about_menu": "<strong>Information about the bot</strong>\n\n"
                          "The developer of this crypto bot is 1 person.\n"
                          "The bot helps track exchange rates from different exchanges and is easy to use.\n\n"
                          "Bot features: \n\n"
                          "<strong>• Viewing exchange rates \n"
                          "• Configuring the exchange \n"
                          "• Configuring the bot language (under development) \n"
                          "• Recommendation algorithm (under development)</strong>",

            "prices_menu": "<strong>Exchange rates</strong>",

            "settings_menu_currency": f"<strong>Bot currency settings</strong>\n\n"
                                       f"Selected currency: {user_settings_currency}"
        }
    }

    return description_for_info_pages.get(language, description_for_info_pages["ru"])

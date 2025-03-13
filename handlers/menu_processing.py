from sqlalchemy.ext.asyncio import AsyncSession

from kbds.inline import (
    get_user_main_btns, 
    get_user_settings_btns,
    get_user_about_btns,
    get_user_prices_btns,
)

from common.text_for_bot import description_for_info_pages_russian

async def main_menu(session: AsyncSession, level: int, menu_name: str):
    description = description_for_info_pages_russian["main_menu"]
    kbds = get_user_main_btns(level=level)
    
    return description, kbds

async def prices_menu(session: AsyncSession, level: int, menu_name: str):
    description = description_for_info_pages_russian["prices_menu"]
    kbds = get_user_prices_btns(level=level)
    
    return description, kbds

async def about_menu(session: AsyncSession, level: int, menu_name: str):
    description = description_for_info_pages_russian["about_menu"]
    kbds = get_user_about_btns(level=level)
    
    return description, kbds

async def settings_menu(session: AsyncSession, level: int, menu_name: str):
    description = description_for_info_pages_russian["settings"]
    kbds = get_user_settings_btns(level=level)
    
    return description, kbds


async def get_menu_content(
    session: AsyncSession,
    level: int,
    menu_name: str,
    page: int | None = None,
    user_id: int | None = None
):
    if level == 0:
        return await main_menu(session, level, menu_name)
    
    if level == 1:
        return await prices_menu(session, level, menu_name)
    
    if level == 2:
        return await about_menu(session, level, menu_name)
    
    if level == 3:
        return await settings_menu(session, level, menu_name)

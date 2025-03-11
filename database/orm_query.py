from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from database.models import User

async def orm_add_user(
    session: AsyncSession,
    user_id: int,
    first_name: str | None = None,
    last_name: str | None = None,
    phone: str | None = None,
):
    query = select(User).where(User.user_id == user_id)
    result = await session.execute(query)
    
    if result.scalars().first() is None:
        new_user = User(user_id=user_id, first_name=first_name, last_name=last_name, phone=phone)
        session.add(new_user)
        
        await session.flush()
        await session.commit()
        
        return new_user

    return None 
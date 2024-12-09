from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from . import models, schemas

async def create_todo(db: AsyncSession, todo: schemas.TodoCreate):
    db_todo = models.Todo(name=todo.name, description=todo.description)
    db.add(db_todo)
    await db.commit()  
    await db.refresh(db_todo) 
    return db_todo

async def get_todos(db: AsyncSession):
    result = await db.execute(select(models.Todo)) 
    return result.scalars().all() 

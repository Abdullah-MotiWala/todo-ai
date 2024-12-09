from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app import models, schemas, crud, database
from app.database import SessionLocal

async def get_db():
    async with SessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()

async def init_db():
    async with database.engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)

app = FastAPI(title="TODO with API of AI",version="0.0.1",servers=[{
    "url":"https://todo-ai.loca.lt/",
    "description":"TODO with API of AI"	
}])

@app.on_event("startup")
async def on_startup():
    await init_db()

@app.post("/todos/", response_model=schemas.Todo)
async def create_todo(todo: schemas.TodoCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_todo(db, todo)

@app.get("/todos/", response_model=list[schemas.Todo])
async def read_todos(db: AsyncSession = Depends(get_db)):
    return await crud.get_todos(db)


@app.get("/")
async def hello():
    return {"hello": "world"}
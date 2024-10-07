from app.models.user import User
from app.models.task import Task

from app.backend.db import engine

from app.backend.db import Base

# Создание всех таблиц
Base.metadata.create_all(bind=engine)

# Вывод SQL-запросов для создания таблиц
#print(CreateTable(Task.__table__))
#print(CreateTable(User.__table__))
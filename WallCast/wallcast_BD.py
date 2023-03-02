from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///users.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    password = Column(String(50))

    def __repr__(self):
        return f'<User {self.username}>'


Base.metadata.create_all(engine)

# Получаем всех пользователей из базы данных
users = session.query(User).all()
for user in users:
    print(user.id, user.username, user.password)

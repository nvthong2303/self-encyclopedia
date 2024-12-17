from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
import datetime

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    age = Column(Integer, nullable=False)
    address = Column(String, nullable=False)

    created_at = Column(DateTime, default=datetime.datetime.utcnow)


class Posts(Base):
    __tablename__ = 'postes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    user = relationship('User', back_populates='posts')

    created_at = Column(DateTime, default=datetime.datetime.utcnow)


User.posts = relationship('Post', back_populates='user')


DATABASE_URL = "postgresql+psycopg2://user-name:strong-password@127.0.0.1:5432/postgresql_test"
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

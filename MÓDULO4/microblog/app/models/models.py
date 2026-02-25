from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, ForeignKey, DateTime
from datetime import datetime
from app import db, login
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(64), index=True, unique=True)
    password: Mapped[str] = mapped_column(String(256))
    foto: Mapped[str] = mapped_column(String(256), nullable=True)
    bio: Mapped[str] = mapped_column(String(500), nullable=True)
    last_login: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=True)
    
    posts: Mapped[list['Post']] = relationship(back_populates='author')

class Post(db.Model):
    __tablename__ = 'posts'
    id: Mapped[int] = mapped_column(primary_key=True)
    body: Mapped[str] = mapped_column(String(140))
    timestamp: Mapped[datetime] = mapped_column(DateTime, index=True, default=datetime.utcnow)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    
    author: Mapped["User"] = relationship(back_populates='posts')

@login.user_loader
def load_user(id):
    return db.session.get(User, int(id))

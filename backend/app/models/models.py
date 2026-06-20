from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.schemas.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), unique=True, index=True)
    provider = Column(String(50))
    access_token = Column(String)
    refresh_token = Column(String)

    mail_config = relationship(
        "MailConfig",
        back_populates="user",
        uselist=False,
        cascade="all, delete-orphan"
    )
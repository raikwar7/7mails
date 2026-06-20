from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    ForeignKey,
    Identity
)
from sqlalchemy.orm import relationship
from app.schemas.database import Base


class MailConfig(Base):
    __tablename__ = "mail_config"

    id = Column(
        Integer,
        Identity(start=1),
        primary_key=True,
        index=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        unique=True,
        nullable=False
    )

    EMAIL_SERVICE = Column(
        String(50),
        nullable=False,
        default="gmail"
    )

    MAIL_SERVER = Column(
        String(255),
        nullable=False,
        default="smtp.gmail.com"
    )

    MAIL_PORT = Column(
        Integer,
        nullable=False,
        default=587
    )

    MAIL_USE_TLS = Column(
        Boolean,
        default=True
    )

    MAIL_USERNAME = Column(
        String(255),
        nullable=False
    )

    MAIL_PASSWORD = Column(
        String(255),
        nullable=False
    )

    user = relationship(
        "User",
        back_populates="mail_config"
    )
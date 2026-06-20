from sqlalchemy import (
    Column,
    BigInteger,
    String,
    Text,
    Boolean,
    Identity
)
from sqlalchemy.dialects.postgresql import JSONB
from app.schemas.database import Base


class Email(Base):
    __tablename__ = "emails"

    id = Column(
        BigInteger,
        Identity(start=1),
        primary_key=True,
        index=True
    )

    # Gmail identifiers
    message_id = Column(String(255), unique=True, index=True)
    thread_id = Column(String(255), index=True)
    history_id = Column(String(255))

    # Email metadata
    sender = Column(Text)
    to_recipients = Column(JSONB)
    cc_recipients = Column(JSONB)
    bcc_recipients = Column(JSONB)
    reply_to = Column(Text)

    subject = Column(Text)
    snippet = Column(Text)

    # Body
    body_text = Column(Text)
    body_html = Column(Text)

    # Attachments
    has_attachments = Column(Boolean, default=False)
    attachments = Column(JSONB)

    # Labels & metadata
    label_ids = Column(JSONB)
    size_estimate = Column(BigInteger)
    internal_date = Column(BigInteger)

    # Raw backup
    raw_headers = Column(JSONB)
    raw_payload = Column(JSONB)
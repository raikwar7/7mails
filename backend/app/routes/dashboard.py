"""
dashboard.py
------------

Dashboard APIs for:

1. Get unique senders for a receiver
2. Get unique receivers for a sender
3. Get filtered sent mails
4. Get filtered received mails

NOTE:
------
to_recipients, cc_recipients and bcc_recipients
are stored as PostgreSQL JSONB.

LIKE cannot be used directly on JSONB.

Therefore:

    Email.to_recipients.like(...)

is WRONG.

Use:

    cast(Email.to_recipients, String).like(...)

instead.
"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import (
    or_,
    distinct,
    cast,
    String
)

from datetime import datetime
from typing import Optional

from app.routes.user import get_db
from app.models.gmailData import Email


router = APIRouter()


# ============================================================
# Get unique senders for a receiver
# ============================================================

@router.get("/mailDashboard/receivers/{email}")
def get_senders_for_receiver_dashboard(
    email: str,
    db: Session = Depends(get_db)
):
    """
    Returns all unique senders who sent mails
    to the specified receiver.
    """

    senders = (
        db.query(distinct(Email.sender))
        .filter(
            or_(
                cast(
                    Email.to_recipients,
                    String
                ).like(f"%{email}%"),

                cast(
                    Email.cc_recipients,
                    String
                ).like(f"%{email}%"),

                cast(
                    Email.bcc_recipients,
                    String
                ).like(f"%{email}%")
            )
        )
        .all()
    )

    sender_list = [s[0] for s in senders if s[0]]

    return {
        "senders": sender_list
    }


# ============================================================
# Get unique receivers for a sender
# ============================================================

@router.get("/mailDashboard/senders/{email}")
def get_receivers_for_sender_dashboard(
    email: str,
    db: Session = Depends(get_db)
):
    """
    Returns all unique recipients
    to whom a sender has sent emails.
    """

    mails = (
        db.query(Email)
        .filter(
            Email.sender.like(f"%{email}%")
        )
        .all()
    )

    receivers_set = set()

    for mail in mails:

        for field in [

            mail.to_recipients,
            mail.cc_recipients,
            mail.bcc_recipients

        ]:

            if field:

                if isinstance(field, list):

                    receivers_set.update(field)

                else:

                    receivers_set.update(
                        field.split(",")
                    )

    receivers_list = [

        r.strip()

        for r in receivers_set

        if r
    ]

    return {

        "receivers": receivers_list

    }


# ============================================================
# Get filtered sent mails
# ============================================================

@router.get("/mailDashboard/sent/{email}")
def get_sent_mail_filtered(

    email: str,

    start: Optional[datetime] = None,

    to: Optional[datetime] = None,

    receiver: Optional[str] = None,

    db: Session = Depends(get_db)

):
    """
    Returns sent mails for a sender.

    Optional filters:

    - start date
    - end date
    - receiver email
    """

    query = db.query(Email).filter(

        Email.sender.like(f"%{email}%")

    )

    # Receiver filter

    if receiver:

        query = query.filter(

            or_(

                cast(
                    Email.to_recipients,
                    String
                ).like(f"%{receiver}%"),

                cast(
                    Email.cc_recipients,
                    String
                ).like(f"%{receiver}%"),

                cast(
                    Email.bcc_recipients,
                    String
                ).like(f"%{receiver}%")

            )

        )

    # Date filters

    if start:

        from_ = int(

            start.timestamp() * 1000

        )

        query = query.filter(

            Email.internal_date >= from_

        )

    if to:

        to_ = int(

            to.timestamp() * 1000

        )

        query = query.filter(

            Email.internal_date <= to_

        )

    mails = (

        query

        .order_by(

            Email.internal_date.desc()

        )

        .all()

    )

    return {

        "mails": mails,

        "count": len(mails)

    }


# ============================================================
# Get filtered received mails
# ============================================================

@router.get("/mailDashboard/received/{email}")
def get_received_mails_filtered(

    email: str,

    start: Optional[datetime] = None,

    to: Optional[datetime] = None,

    sender: Optional[str] = None,

    db: Session = Depends(get_db)

):
    """
    Returns received mails for a receiver.

    Optional filters:

    - sender
    - start date
    - end date
    """

    query = db.query(Email)

    query = query.filter(

        or_(

            cast(
                Email.to_recipients,
                String
            ).like(f"%{email}%"),

            cast(
                Email.cc_recipients,
                String
            ).like(f"%{email}%"),

            cast(
                Email.bcc_recipients,
                String
            ).like(f"%{email}%")

        )

    )

    if sender:

        query = query.filter(

            Email.sender.like(

                f"%{sender}%"

            )

        )

    if start:

        from_ = int(

            start.timestamp() * 1000

        )

        query = query.filter(

            Email.internal_date >= from_

        )

    if to:

        to_ = int(

            to.timestamp() * 1000

        )

        query = query.filter(

            Email.internal_date <= to_

        )

    mails = (

        query

        .order_by(

            Email.internal_date.desc()

        )

        .all()

    )

    return {

        "mails": mails,

        "count": len(mails)

    }
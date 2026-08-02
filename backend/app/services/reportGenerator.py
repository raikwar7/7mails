from datetime import datetime, date, time
from typing import Optional

from fastapi import Depends
from sqlalchemy import or_, cast, String
from sqlalchemy.orm import Session

from app.models.gmailData import Email
from app.routes.user import get_db


def generate_daily_report(
    user_email: str,
    db: Session = Depends(get_db),
    start_date: Optional[datetime] = None,
    end_date: Optional[datetime] = None,
):
    """
    Generate a daily email report for a specific user.

    The report contains:
    - All emails received by the user
    - All emails sent by the user
    - Total email count within the given date range

    If start_date and end_date are not provided,
    the report defaults to the current day.
    """

    # ---------------------------------------------------------
    # 1. Set default date range
    # ---------------------------------------------------------
    if start_date is None:
        start_date = datetime.combine(
            date.today(),
            time.min
        )

    if end_date is None:
        end_date = datetime.combine(
            date.today(),
            time.max
        )

    # ---------------------------------------------------------
    # 2. Convert datetime to timestamp in milliseconds
    #
    # Gmail internalDate is generally stored as milliseconds
    # since Unix epoch.
    # ---------------------------------------------------------
    start_timestamp = int(start_date.timestamp() * 1000)
    end_timestamp = int(end_date.timestamp() * 1000)

    # ---------------------------------------------------------
    # 3. Base query
    #
    # Fetch only emails that fall within the requested
    # date range.
    # ---------------------------------------------------------
    base_query = db.query(Email).filter(
        Email.internal_date >= start_timestamp,
        Email.internal_date <= end_timestamp
    )

    # ---------------------------------------------------------
    # 4. Query received emails
    #
    # An email is considered received if the user's email
    # appears in To, CC, or BCC recipients.
    # ---------------------------------------------------------
    received_mails_query = base_query.filter(
        or_(
            cast(Email.to_recipients, String).like(
                f"%{user_email}%"
            ),
            cast(Email.cc_recipients, String).like(
                f"%{user_email}%"
            ),
            cast(Email.bcc_recipients, String).like(
                f"%{user_email}%"
            )
        )
    )

    # ---------------------------------------------------------
    # 5. Query sent emails
    #
    # An email is considered sent if the user's email
    # appears in the sender field.
    # ---------------------------------------------------------
    sent_mails_query = base_query.filter(
        Email.sender.like(f"%{user_email}%")
    )

    # ---------------------------------------------------------
    # 6. Execute received emails query
    # ---------------------------------------------------------
    filtered_mails_received = (
        received_mails_query
        .order_by(Email.internal_date.desc())
        .all()
    )

    # ---------------------------------------------------------
    # 7. Execute sent emails query
    # ---------------------------------------------------------
    filtered_mails_sent = (
        sent_mails_query
        .order_by(Email.internal_date.desc())
        .all()
    )

    # ---------------------------------------------------------
    # 8. Execute query for all emails
    # ---------------------------------------------------------
    filtered_mails = (
        base_query
        .order_by(Email.internal_date.desc())
        .all()
    )

    # ---------------------------------------------------------
    # 9. Return report data
    # ---------------------------------------------------------
    return {
        "mails": filtered_mails,

        "received_mails": filtered_mails_received,
        "received_mails_count": len(filtered_mails_received),

        "sent_mails": filtered_mails_sent,
        "sent_mails_count": len(filtered_mails_sent),

        "total_mails_count": len(filtered_mails),

        "start_date": start_date,
        "end_date": end_date,
    }
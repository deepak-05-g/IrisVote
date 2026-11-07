from datetime import date, datetime

from sqlalchemy import Date, DateTime, Index, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class Registration(Base):
    __tablename__ = "registrations"
    __table_args__ = (Index("ix_registrations_synthetic_voter_id", "synthetic_voter_id"),)

    id: Mapped[int] = mapped_column(primary_key=True)
    synthetic_voter_id: Mapped[str] = mapped_column(String(9), unique=True)
    full_name: Mapped[str] = mapped_column(String(120))
    date_of_birth: Mapped[date] = mapped_column(Date)
    address: Mapped[str] = mapped_column(Text)
    contact_number: Mapped[str | None] = mapped_column(String(20), nullable=True)
    status: Mapped[str] = mapped_column(String(32), default="PENDING_REVIEW")
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

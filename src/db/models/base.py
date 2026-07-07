from sqlalchemy.orm import DeclarativeBase ,Mapped, mapped_column
from datetime import datetime, UTC
from sqlalchemy import DateTime

class TimestampMixin():
    created:Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC)
    )
    updated:Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC),
        onupdate=lambda: datetime.now(UTC)
    )


class Base(DeclarativeBase,TimestampMixin): pass
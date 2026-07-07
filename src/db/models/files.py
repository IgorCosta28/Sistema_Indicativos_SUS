from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.models.base import Base


class Files(Base):
    __tablename__ = "files"

    id: Mapped[int] = mapped_column(primary_key=True)
    indicative: Mapped[str]
    name: Mapped[str]
    path: Mapped[str]
    status: Mapped[str]
    group_id: Mapped[int] = mapped_column(ForeignKey("groups.id"))

    groups: Mapped["Groups"] = relationship(back_populates="files")

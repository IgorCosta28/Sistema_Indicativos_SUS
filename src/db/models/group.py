from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.models.base import Base


class Groups(Base):
    __tablename__ = "groups"
    id: Mapped[int] = mapped_column(primary_key=True)
    year: Mapped[int]
    periodic: Mapped[int]
    team: Mapped[int]
    uuid: Mapped[int]

    files: Mapped[list["Files"]] = relationship(
        back_populates="groups", cascade="all, delete-orphan"
    )

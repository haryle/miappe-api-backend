from typing import TYPE_CHECKING, Optional
from uuid import UUID

from litestar.dto import dto_field
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from miappe.model.base import Base

if TYPE_CHECKING:
    from miappe.model.biological_material import BiologicalMaterial
    from miappe.model.device import Device
    from miappe.model.vocabulary import Vocabulary


class Method(Base):
    __tablename__: str = "method_table"  # type: ignore

    # Relationships:
    method_type_id: Mapped[Optional[UUID]] = mapped_column(
        ForeignKey("vocabulary_table.id")
    )
    method_type: Mapped[Optional["Vocabulary"]] = relationship(
        back_populates="method", lazy="selectin", info=dto_field("read-only")
    )

    device_id: Mapped[Optional[UUID]] = mapped_column(ForeignKey("device_table.id"))
    device: Mapped[Optional["Device"]] = relationship(
        back_populates="method", lazy="selectin", info=dto_field("read-only")
    )

    biological_material: Mapped[Optional["BiologicalMaterial"]] = relationship(
        back_populates="preprocessing_method",
        lazy="selectin",
        info=dto_field("read-only"),
    )
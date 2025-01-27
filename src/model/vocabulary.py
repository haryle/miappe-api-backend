from typing import TYPE_CHECKING

from litestar.dto import dto_field
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.model.base import Base

__all__ = ("Vocabulary",)


if TYPE_CHECKING:
    from src.model.biological_material import BiologicalMaterial
    from src.model.device import Device
    from src.model.event import Event
    from src.model.experiment import Experiment
    from src.model.experimental_factor import ExperimentalFactor
    from src.model.facility import Facility
    from src.model.institution import Institution
    from src.model.method import Method
    from src.model.observation_unit import ObservationUnit
    from src.model.observed_variable import ObservedVariable
    from src.model.sample import Sample
    from src.model.unit import Unit


class Vocabulary(Base):
    __tablename__: str = "vocabulary_table"
    title: Mapped[str]
    # Todo: use the same terminologies as PHIS - extract, widening, narrowing?
    relationship_type: Mapped[str | None]
    accession_number: Mapped[str | None]
    external_reference: Mapped[str | None]

    # Todo: Make namespace a separate entity?
    namespace: Mapped[str | None] = mapped_column(server_default="APPN")

    # # Relationships
    device: Mapped[list["Device"]] = relationship(
        back_populates="device_type",
        lazy=None,
        info=dto_field("read-only"),
    )
    method: Mapped[list["Method"]] = relationship(
        back_populates="method_reference",
        lazy=None,
        info=dto_field("read-only"),
    )
    unit: Mapped[list["Unit"]] = relationship(
        back_populates="unit_reference",
        lazy=None,
        info=dto_field("read-only"),
    )
    factor_type: Mapped[list["ExperimentalFactor"]] = relationship(
        back_populates="factor_type",
        lazy=None,
        info=dto_field("read-only"),
    )
    event: Mapped[list["Event"]] = relationship(
        back_populates="event_type",
        lazy=None,
        info=dto_field("read-only"),
    )
    sample_plant_structural_development_stage: Mapped[list["Sample"]] = relationship(
        back_populates="plant_structural_development_stage",
        lazy=None,
        foreign_keys="[Sample.plant_structural_development_stage_id]",
        info=dto_field("read-only"),
    )
    sample_plant_anatomical_entity: Mapped[list["Sample"]] = relationship(
        back_populates="plant_anatomical_entity",
        foreign_keys="[Sample.plant_anatomical_entity_id]",
        lazy=None,
        info=dto_field("read-only"),
    )
    facility: Mapped[list["Facility"]] = relationship(
        back_populates="facility_type",
        lazy=None,
        info=dto_field("read-only"),
    )
    institution: Mapped[list["Institution"]] = relationship(
        back_populates="institution_type",
        lazy=None,
        info=dto_field("read-only"),
    )
    experiment: Mapped[list["Experiment"]] = relationship(
        back_populates="experiment_type",
        lazy=None,
        info=dto_field("read-only"),
    )
    organism: Mapped[list["BiologicalMaterial"]] = relationship(
        back_populates="organism",
        lazy=None,
        info=dto_field("read-only"),
    )
    trait_reference: Mapped[list["ObservedVariable"]] = relationship(
        lazy=None,
        back_populates="trait_reference",
        info=dto_field("read-only"),
        foreign_keys="[ObservedVariable.trait_reference_id]",
    )
    observation_unit: Mapped[list["ObservationUnit"]] = relationship(
        back_populates="observation_unit_type",
        lazy=None,
        info=dto_field("read-only"),
    )

"""Typed data models used by the RANOpt foundation."""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field, field_validator


class RANKPI(BaseModel):
    """Technology-neutral KPI snapshot for one cell and timestamp."""

    model_config = ConfigDict(extra="forbid")

    cell_id: str = Field(min_length=1)
    timestamp: datetime
    rsrp_dbm: float
    rsrq_db: float
    sinr_db: float
    dl_throughput_mbps: float = Field(ge=0)
    ul_throughput_mbps: float = Field(ge=0)
    drop_rate_pct: float = Field(ge=0, le=100)
    handover_success_pct: float = Field(ge=0, le=100)
    availability_pct: float = Field(ge=0, le=100)

    @field_validator("cell_id")
    @classmethod
    def normalize_cell_id(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("cell_id cannot be empty")
        return value


class CellRecord(BaseModel):
    """Optional cell metadata kept separate from KPI observations."""

    model_config = ConfigDict(extra="forbid")

    cell_id: str = Field(min_length=1)
    site_id: str = Field(min_length=1)
    sector: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None

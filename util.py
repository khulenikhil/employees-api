from typing import Any
import enum
from pydantic import BaseModel
from datetime import date


class GenderEnum(enum.Enum):
    M = "M"
    F = "F"


class UpdateResponseModel(BaseModel):
    emp_no: int
    field_name: str
    field_value: Any

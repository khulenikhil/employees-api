from pydantic import BaseModel
from datetime import date
from util import GenderEnum


class Employee(BaseModel):
    emp_no: int
    birth_date: date
    hire_date: date
    first_name: str
    last_name: str
    gender: GenderEnum

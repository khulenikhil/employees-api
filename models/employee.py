from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, Date, String, Enum
from config.db import meta
from util import GenderEnum

employees = Table(
    "employees",
    meta,
    Column("emp_no", Integer, primary_key=True),
    Column("birth_date", Date),
    Column("first_name", String(14)),
    Column("last_name", String(16)),
    Column("gender", Enum(GenderEnum)),
    Column("hire_date", Date),
)

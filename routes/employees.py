from fastapi import APIRouter, HTTPException
from config.db import connection
from models import employees
from schemas import Employee
from datetime import date
from util import *

employees_router = APIRouter()


@employees_router.get("/")
async def get_employees(limit: int = 10):
    return connection.execute(employees.select().limit(limit)).fetchall()


@employees_router.get("/employee/{emp_no}")
def get_employees_by_emp_no(emp_no: int):
    result = connection.execute(
        employees.select().where(employees.c.emp_no == emp_no)
    ).fetchall()
    if len(result) == 0:
        raise HTTPException(
            status_code=404,
            detail=f"Employee with emp_no {emp_no} does not exist.",
        )
    else:
        return {"data": result[0]}


@employees_router.post("/new")
async def post_employee(employee: Employee):
    """
    Create a new employee entry in the table
    """
    try:
        connection.execute(
            employees.insert().values(
                emp_no=employee.emp_no,
                birth_date=employee.birth_date,
                hire_date=employee.hire_date,
                first_name=employee.first_name,
                last_name=employee.last_name,
                gender=employee.gender,
            )
        )
        return {"message": "Details added successfully", "data": employee}
    except Exception as e:
        return {"message": e.args, "error": e}


@employees_router.put("/update")
async def update_employee(update_emp_data: UpdateResponseModel):
    try:
        emp_no, field_name, field_value = (
            update_emp_data.emp_no,
            update_emp_data.field_name,
            update_emp_data.field_value,
        )
        match field_name:
            case "emp_no":
                raise HTTPException(
                    status_code=400, detail={"message": "Cannot change emp_no field."}
                )
            case "first_name":
                connection.execute(
                    employees.update()
                    .where(employees.c.emp_no == emp_no)
                    .values(first_name=field_value)
                )
                return {"message": f"{field_name} updated successfully."}
            case "last_name":
                connection.execute(
                    employees.update()
                    .where(employees.c.emp_no == emp_no)
                    .values(last_name=field_value)
                )
                return {"message": f"{field_name} updated successfully."}
            case "birth_date":
                connection.execute(
                    employees.update()
                    .where(employees.c.emp_no == emp_no)
                    .values(birth_date=field_value)
                )
                return {"message": f"{field_name} updated successfully."}
            case "hire_date":
                connection.execute(
                    employees.update()
                    .where(employees.c.emp_no == emp_no)
                    .values(hire_date=field_value)
                )
                return {"message": f"{field_name} updated successfully."}
            case "gender":
                connection.execute(
                    employees.update()
                    .where(employees.c.emp_no == emp_no)
                    .values(gender=field_value)
                )
                return {"message": f"{field_name} updated successfully."}
            case default:
                raise HTTPException(
                    status_code=400, detail={"message": f"Invalid column: {field_name}"}
                )
    except Exception as e:
        return {"message": e.args, "error": e}


@employees_router.delete("/delete")
async def delete_employee(emp_no: int):
    return connection.execute(employees.delete().where(employees.c.emp_no == emp_no))

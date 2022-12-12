"""
Database configurations
"""

from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://nikhil:Root!123@localhost:3306/employees")
meta = MetaData()

connection = engine.connect()

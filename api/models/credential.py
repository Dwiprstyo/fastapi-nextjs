from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Credential(Base):
    __tablename__ = "cnt_payment_credential"
    id = Column(Integer, primary_key=True, index=True)
    vendor = Column(String(50), index=True)
    company_code = Column(String(50), unique=True, index=True)
    credential_sand = Column(String)
    credential_prod = Column(String)

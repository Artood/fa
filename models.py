from sqlalchemy import Column, Integer, String
from .database import Base

class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    inn = Column(String, unique=True, nullable=False)
    contract_number = Column(String, nullable=True)
    contact_person = Column(String, nullable=True)
    external_prefix = Column(String, nullable=True)
    ip_dmz = Column(String, nullable=True)
    ip_inside = Column(String, nullable=True)


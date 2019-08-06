from uuid import uuid4
from sqlalchemy.dialects.postgresql import JSONB, UUID

from sqlalchemy import Column
from sqlalchemy import String, Integer, LargeBinary
from sqlalchemy.dialects.postgresql import JSONB

from app.model import Base
from app.config import UUID_LEN
from app.utils import alchemy


class Company(Base):
    __tablename__ = "company"

    db_id = Column("id", UUID(True), primary_key=True, default=uuid4)
    name = Column(String, nullable=False)
    vat_no = Column(String)
    contact_number = Column(String)
    company_attributes = Column(JSONB)
    website = Column(String)
    email = Column(String)

    def __repr__(self):
        return f"{self.name}"


    @classmethod
    def get_id(cls):
        return cls.db_id


    FIELDS = {
        "contact_number": str, 
        "name": str, 
        "website": str,
        "email": str,
        "vat_no": str,
        "db_id": str,
        "company_attributes": alchemy.passby
    }

    FIELDS.update(Base.FIELDS)

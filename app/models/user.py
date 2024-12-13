from sqlalchemy import Column, Integer, String, DateTime, Enum
from sqlalchemy.sql import func
from app.core.database import Base
import enum

class AccountStatus(enum.Enum):
    standard = "standard"
    admin = "admin"
    suspended = "suspended"
    banned = "banned"

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    date_created = Column(DateTime(timezone=True), server_default=func.now())
    account_status = Column(Enum(AccountStatus), default=AccountStatus.standard)
    type = Column(Integer, default=0)
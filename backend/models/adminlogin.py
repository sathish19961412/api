from sqlalchemy import Column , Integer , String, ForeignKey
from database import Base
from sqlalchemy.orm import relationship

class User(Base):

    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
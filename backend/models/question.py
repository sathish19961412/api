from sqlalchemy import Column , Integer , String
from database import Base



class Question(Base):

    __tablename__ = "questions"

    question_id = Column ( Integer , primary_key = True , index = True )
    question = Column(String)
    optionA = Column(String)
    optionB = Column(String)
    optionC = Column(String)
    optionD = Column(String)


from pydantic import BaseModel


class CreateQuestions(BaseModel):
    question: str
    optionA: str
    optionB: str
    optionC: str
    optionD: str

    class Config:
        orm_mode = True


class ShowQuestions(BaseModel):
      question_id: int
      question: str
      optionA: str
      optionB: str
      optionC: str
      optionD: str

      class Config ( ):
          orm_mode = True

class QuestionUpdate(CreateQuestions):

    question: str
    optionA: str
    optionB: str
    optionC: str
    optionD: str

    

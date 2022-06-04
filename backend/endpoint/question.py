from typing import List
from fastapi import FastAPI , Depends,HTTPException,status
from database import engine , SessionLocal
from sqlalchemy.orm import Session
from fastapi import APIRouter
from crud import question as crud_question
from schemas import question as schema_question
from models import question as model_question

# app= FastAPI ()
router = APIRouter()

model_question.Base.metadata.create_all( engine )


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get( '/questions',response_model=List[schema_question.ShowQuestions],tags =['Questions'])
def review_all(db: Session = Depends ( get_db )):
    question= crud_question.review_questions(db)
    return question

@router.get("/questions/", response_model=List[schema_question.ShowQuestions],tags=["Questions"])
def get_question(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    question = crud_question.get_users(db,skip=skip, limit=limit)
    return question

@router.get("/questions/{questions_id}", response_model=schema_question.ShowQuestions,tags=["Questions"])
def read_questions(questions_id: int, db: Session = Depends(get_db)):
    question = crud_question.get_questions(db, question_id=questions_id)
    if question is None:
        raise HTTPException(status_code=404, detail="Question not found")
    return question

@router.post("/questions/", response_model=schema_question.ShowQuestions,tags=["Questions"])
def create_question(create_question: schema_question.CreateQuestions, db: Session = Depends(get_db)):
    question = crud_question.get_by_question(db,question=create_question.question)
    if question:
        raise HTTPException(status_code=400, detail="Question Already Created")
    return crud_question.create_question(db=db,questions=create_question)

@router.delete("/questions/{questions_id}/", tags=["Questions"])
def delete_question(question_id:int,db: Session = Depends(get_db)):
   question = crud_question.question_delete(db,question_id=question_id)

   return question

@router.put("/questions/{question_id}",response_model=schema_question.QuestionUpdate,tags=["Questions"])
def update_question(question:schema_question.QuestionUpdate,question_id=int,  db: Session = Depends(get_db)):

    return crud_question.question_update(db=db,question_id=question_id,question=question)

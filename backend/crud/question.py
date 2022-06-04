from sqlalchemy.orm import Session
from schemas import question as schema_question
from models import question as model_question
from models import question

def get_by_question(db: Session,question: str):

    return db.query(model_question.Question).filter(model_question.Question.question== question).first()

def create_question(db: Session, questions: schema_question.CreateQuestions):
    db_question = model_question.Question(question=questions.question,optionA = questions.optionA,optionB = questions.optionB,optionC = questions.optionC,optionD = questions.optionD)
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question

def get_questions(db: Session, question_id: int):

    return db.query(model_question.Question).filter(model_question.Question.question_id==question_id).first()

def review_questions(db:Session):
    return db.query(model_question.Question).all()

def get_users(db: Session, skip: int = 0, limit: int = 100):

    return db.query(model_question.Question).offset(skip).limit(limit).all()

def question_delete(db: Session, question_id: int):

    db_job = db.query(model_question.Question).filter(model_question.Question.question_id==question_id).first()
    db.delete(db_job)
    db.commit()
    return "success"

def question_update(db: Session,question:schema_question.QuestionUpdate,question_id: int):

    db_job =db.query(model_question.Question).filter(model_question.Question.question_id==question_id).first()
    for var, value in vars(question).items():
        setattr(db_job, var, value) if value else None
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job
from sqlalchemy.orm import Session, joinedload
from app.models.subject import Subject
from app.models.exam import Exam
from app.schemas.subject_schema import SubjectRequest


# Subject 생성 함수
def create_subject(db: Session, subject_data: SubjectRequest) -> Subject:
    new_subject = Subject(**subject_data.model_dump())
    db.add(new_subject)
    db.commit()
    db.refresh(new_subject)

    return new_subject


# Subject 조회 함수
def get_subject(db: Session) -> Subject:
    return db.query(Subject).all()


# 단일 Subject 조회 함수
def get_subject_by_id(db: Session, subject_id: int) -> Subject:
    return db.query(Subject).filter(Subject.subject_id == subject_id).first()


# Subject에 속한 Exams 조회 함수
def get_exams_by_subject(db: Session, subject_id: int) -> Exam:
    subject = db.query(Subject).options(joinedload(Subject.exams)).filter(Subject.subject_id == subject_id).first()
    return subject.exams


# Subject 수정 함수
def patch_subject_by_id(db: Session, subject_id: int, subject_data: SubjectRequest) -> Subject:
    patched_subject = get_subject_by_id(db, subject_id)

    if patched_subject:
        update_data = subject_data.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(patched_subject, key, value)

    db.commit()
    db.refresh(patched_subject)

    return patched_subject


# Subject 삭제 함수
def delete_subject_by_id(db: Session, subject_id: int) -> Subject:
    subject = get_subject_by_id(db, subject_id)
    if subject:
        db.delete(subject)
        db.commit()

    return subject
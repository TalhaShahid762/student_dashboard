from sqlalchemy import Column, Integer, String
from db.database import Base

class Schedule(Base):
    __tablename__ = 'schedules'

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer)
    schedule = Column(String)

    def __repr__(self):
        return f"<Schedule(id={self.id}, student_id={self.student_id}, schedule={self.schedule})>"

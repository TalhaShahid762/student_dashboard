from sqlalchemy import Column, Integer, String
from db.database import Base

class ProgressReport(Base):
    __tablename__ = 'progress_reports'

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer)
    report = Column(String)

    def __repr__(self):
        return f"<ProgressReport(id={self.id}, student_id={self.student_id}, report={self.report})>"

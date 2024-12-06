from sqlalchemy import Column, Integer, String
from db.database import Base

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)

    def __repr__(self):
        return f"<Student(id={self.id}, name={self.name}, age={self.age})>"

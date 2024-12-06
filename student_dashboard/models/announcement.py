from sqlalchemy import Column, Integer, String
from db.database import Base

class Announcement(Base):
    __tablename__ = 'announcements'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)

    def __repr__(self):
        return f"<Announcement(id={self.id}, title={self.title}, content={self.content})>"

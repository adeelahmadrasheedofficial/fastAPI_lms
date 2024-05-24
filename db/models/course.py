from datetime import datetime
from sqlalchemy_utils import URLType
from .mixins import Timestamp
from .user import User
import enum
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from ..db_setup import Base

class ContentType(enum.Enum):
    lesson = 1
    quiz = 2
    assignment = 3

class Course(Timestamp, Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    created_by = relationship(User)
    section = relationship("Section", back_populates="course", uselist=False)
    student_course = relationship("StudentCourse", back_populates="course")

class Section(Timestamp, Base):
    __tablename__ = "sections"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=True)
    course_id = Column(Integer, ForeignKey("courses.id"), nullable=False)

    course = relationship("Course", back_populates="section")
    content_block = relationship("ContentBlock", back_populates="section")

class ContentBlock(Timestamp, Base):
    __tablename__ = "content_blocks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=True)
    type = Column(Enum(ContentType))
    url = Column(URLType, nullable=True)
    content = Column(Text, nullable=True)
    section_id = Column(Integer, ForeignKey("sections.id"), nullable=False)

    section = relationship("Section", back_populates="content_block")
    completed_content_blocks = relationship("CompletedContentBlock", back_populates="content")

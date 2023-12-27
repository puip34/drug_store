from sqlalchemy import Column, Integer, String, Text, Date, ForeignKey, create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

# User model
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    password = Column(String)
    role = Column(String, index=True)

# Drug model
class Drug(Base):
    __tablename__ = "drugs"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(Text)

# Application model
class Application(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True, index=True)
    number = Column(String, index=True)
    date_added = Column(Date, default=func.now())
    drug_id = Column(Integer, ForeignKey("drugs.id"))
    customer_data = Column(String)
    status = Column(String)
    # Add other fields as needed

    drug = relationship("Drug", back_populates="applications")

# Seller model
class Seller(Base):
    __tablename__ = "sellers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    # Add other fields as needed

# Comment model
class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    application_id = Column(Integer, ForeignKey("applications.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    comment_text = Column(Text)
    timestamp = Column(Date, default=func.now())

    application = relationship("Application", back_populates="comments")
    user = relationship("User", back_populates="comments")

# Add other models as needed

# Define the relationship between Drug and Application
Drug.applications = relationship("Application", back_populates="drug")

# Define the relationship between Application and Comment
Application.comments = relationship("Comment", back_populates="application")

# Create the SQLite database engine
DATABASE_URL = "sqlite:///./drug_store.db"
engine = create_engine(DATABASE_URL)

# Create tables
Base.metadata.create_all(bind=engine)

#Imports
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, DateTime, ForeignKey, func


#Initialise the database
db = SQLAlchemy()

#Create tables via Model classes
class User(db.Model):
    __tablename__ = "users"

    id:Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name:Mapped[str] = mapped_column(String(50))
    email:Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    username:Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    password:Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    role:Mapped[str] = mapped_column(String(30), nullable=False)
    reset_token:Mapped[str] = mapped_column(String(20), nullable=True)
    reset_token_expiration:Mapped[DateTime] = mapped_column(DateTime, nullable=True)
    
   

 


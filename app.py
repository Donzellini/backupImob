from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, String, MetaData, Integer
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:dragoncross9@localhost:5432/Prova'
engine = create_engine("postgresql://postgres:dragoncross9@localhost:5432/Prova")

Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()

# class User(Base):
#     __tablename__ = 'users'
    
#     id = Column(Integer, primary_key=True)
#     name = Column(String(255), nullable=False)
#     email = Column(String, nullable=False)

# Base.metadata.create_all(engine)

# admin = User(id=1, name='admin', email='admin@example.com')
# user = User(id=2, name='user', email='user@example.com')
# client = User(id=3, name='client', email='client@sample.com')

# session.add(admin)
# session.add(user)
# session.add(client)

# session.commit()

session.execute('DROP TABLE users')
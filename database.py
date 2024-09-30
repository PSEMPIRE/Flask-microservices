import os
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Item(Base):
    __tablename__ = 'items'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)

    def __repr__(self):
        return f"<Item(id={self.id}, name='{self.name}')>"

# Get the absolute path to the directory containing this file
base_dir = os.path.abspath(os.path.dirname(__file__))
# Construct the full path to the database file
db_path = os.path.join(base_dir, 'shared.db')

engine = create_engine(f'sqlite:///{db_path}', echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)


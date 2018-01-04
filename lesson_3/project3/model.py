from SQLAlchemy import Column, Integer, String
from SQLAlchemy.ext.declarative import declarative_base
from SQLAlchemy import create_engine

Base = declarative_base()

class Puppy(Base):
    __tablename__ = 'puppy'
    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))

engine = create_engine('sqlite:///puppies.db')
Base.metadata.create_all(engine)
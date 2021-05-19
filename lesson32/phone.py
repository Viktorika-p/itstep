from sqlalchemy import create_engine, engine
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship, backref
from datetime import date

from sqlalchemy.sql.sqltypes import INTEGER


engine = create_engine('sqlite:///database.sqlite', echo=True)
Session = sessionmaker(bind=engine)

Base = declarative_base()

class Phone(Base):
    __tablename__ = "Phone"

    id = Column(Integer, primary_key=True)
    company = Column(String)
    model = Column(Date)
    size = Column(INTEGER)
    price = Column(INTEGER)


    def __init__(self, company, model, size, price) -> None:
        self.company = company
        self.model = model
        self.size = size
        self.price = price

# storage/models.py

from sqlalchemy import create_engine, Column, Integer, String, DECIMAL, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from config.settings import DATABASE_URL
Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurants'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    location = Column(String)

    menu_items = relationship('MenuItem', back_populates='restaurant')

class MenuItem(Base):
    __tablename__ = 'menu_items'
    id = Column(Integer, primary_key=True)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    item_name = Column(String)
    price = Column(DECIMAL)

    restaurant = relationship('Restaurant', back_populates='menu_items')
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)

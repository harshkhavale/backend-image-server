# storage/db.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from storage.models import Restaurant, MenuItem, Base
from config.settings import DATABASE_URL

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

def insert_restaurant(name, location):
    restaurant = Restaurant(name=name, location=location)
    session.add(restaurant)
    session.commit()
    return restaurant.id

def insert_menu_item(restaurant_id, item_name, price):
    menu_item = MenuItem(restaurant_id=restaurant_id, item_name=item_name, price=price)
    session.add(menu_item)
    session.commit()

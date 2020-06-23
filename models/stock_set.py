from app import db
from sqlalchemy.dialects.postgresql import JSON, NUM, STR, DATE


class StockSet(db.Model):
    __tablename__ = 'stock_set'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(), nullable=True)
    first_price = db.Column(NUM)
    last_price = db.Column(NUM)
    first_date = db.Columnn(DATE)
    last_date = db.Column(DATE)

    def __init__(self, url, first_price, last_price, first_date, last_date):
        self.url = url
        self.first_price = first_price
        self.last_price = last_price
        self.first_date = first_date
        self.last_date = last_date
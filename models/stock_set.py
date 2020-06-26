from app import db


class StockSet(db.Model):
    __tablename__ = 'stock_set'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(), nullable=True)
    name = db.Column(db.String())
    ticker = db.Column(db.String())
    first_price = db.Column(db.Numeric())
    last_price = db.Column(db.Numeric())
    first_date = db.Column(db.Date())
    last_date = db.Column(db.Date())

    def __init__(self, url, first_price, last_price, first_date, last_date, name, ticker):
        self.url = url
        self.first_price = first_price
        self.last_price = last_price
        self.first_date = first_date
        self.last_date = last_date
        self.name = name
        self.ticker = ticker

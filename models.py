def create_classes(db):
    class Meat(db.Model):
        __tablename__ = 'meat'

        id = db.Column(db.Integer, primary_key=True)
        year = db.Column(db.Float)
        beef = db.Column(db.Float)
        lamb = db.Column(db.Float)
        pork = db.Column(db.Float)
        chicken = db.Column(db.Float)
        

        def __repr__(self):
            return '<Meat %r>' % (self.year)
    return Meat

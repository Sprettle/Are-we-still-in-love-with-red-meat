def create_classes(db):
    class Meat(db.Model):
        __tablename__ = 'meat'

        id = db.Column(db.Integer, primary_key=True)
        year = db.Column(db.Int)
        beef = db.Column(db.Int)
        lamb = db.Column(db.Int)
        pork = db.Column(db.Int)
        chicken = db.Column(db.Int)
        

        def __repr__(self):
            return '<Meat %r>' % (self.year)
    return Meat

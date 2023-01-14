from application import db


class Policies(db.Model):
    __tablename__ = 'policies'
    __table_args__ = {
        'autoload': True,
        'autoload_with': db.engine
    }

from application import db


class Accounts(db.Model):
    __tablename__ = 'accounts'
    __table_args__ = {
        'autoload': True,
        'autoload_with': db.get_engine(bind="policy")
    }

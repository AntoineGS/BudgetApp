from app import login, db
from flask_login import UserMixin
import uuid


# flask db migrate -m "comment"
# flask db upgrade

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    use_in_budget = db.Column(db.Boolean)

    def __repr__(self):
        return '<Category {}>'.format(self.name)

    def add_manual_transaction(self, date, description, amount):
        bank_transaction = BankTransaction(account_id='MANUAL', transaction_date=date, amount=amount,
                                           category_id=self.id, description=description,
                                           transaction_id=uuid.uuid1())
        db.database.add(bank_transaction)
        db.session.commit()


class BankTransaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.String(64))  # includes a prefix with bank for now
    # ID used by bank to uniquely identify record, for reconciliation
    transaction_id = db.Column(db.String(250))
    transaction_date = db.Column(db.Date)
    amount = db.Column(db.Float)  # +/-ve, not using 2 fields for debit/credit
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))  # going to FK to category table
    description = db.Column(db.String(250))
    db.Index('account_transaction_id', account_id, transaction_id)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))

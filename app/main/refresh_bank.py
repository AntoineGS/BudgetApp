import cibc
from app import config, db
from app.models import BankTransaction
from datetime import date
from flask import flash
from dateutil import parser


def refresh_bank():
    count = 0
    c = cibc.CIBC(config.cibcUsername, config.cibcPassword)
    c.Accounts()  # downloads account headers
    c.gTransactions(date(year=2020, month=1, day=1), date.today())  # download transactions

    # todo: need to remove transactions that have disappeared too, like pre-auth checks
    for account in c.accounts:
        for transaction in account.transactions:
            bank_transaction = BankTransaction.query.filter_by(
                account_id=account.id, transaction_id=transaction.fitId).first()

            # if we don't have it we insert it
            if not bank_transaction:
                count += 1
                amount = transaction.debit * -1 if transaction.debit is not None else transaction.credit
                bank_transaction = BankTransaction(account_id=account.id, transaction_id=transaction.fitId,
                                                   transaction_date=parser.parse(transaction.date), amount=amount,
                                                   description=transaction.transactionDescription)
                db.session.add(bank_transaction)

    db.session.commit()
    return count

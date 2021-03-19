import uuid
from dataclasses import dataclass
from datetime import datetime, timedelta

import pyqiwi

from data import variable

wallet = pyqiwi.Wallet(token=variable.QIWI_TOKEN, number=variable.WALLET_QIWI)


class NotEnoughMoney(Exception):
    pass


class NotPaymentFound(Exception):
    pass


@dataclass
class Payment:
    amount: int
    id: str = None

    def create(self):
        self.id = str(uuid.uuid4())

    def check_payment(self):
        transactions = wallet.history(rows=50,
                                      start_date=datetime.now()-timedelta(minutes=30),
                                      end_date=datetime.now()).get("transactions")
        for transaction in transactions:
            if str(self.id) in transaction.comment:
                if float(transaction.total.amount) >= 0:
                    print(transaction.total.amount)
                    return transaction.total.amount
                else:
                    raise NotEnoughMoney
        else:
            raise NotPaymentFound

    @property
    def invoice(self):
        link = 'https://oplata.qiwi.com/create?publicKey={pubkey}&amount={amount}&comment={comment}'
        return link.format(pubkey=variable.QIWI_PUBKEY, amount=self.amount, comment=self.id)
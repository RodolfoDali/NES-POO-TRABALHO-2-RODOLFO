from finances.core import Account
from datetime import datetime, timedelta

def test_account_initialization():
    account = Account(name="Conta Corrente")
    assert account.name == "Conta Corrente"
    assert account.balance == 0.0
    assert len(account.transactions) == 0

def test_add_transaction():
    account = Account(name="Conta Poupança")
    transaction = account.add_transaction(amount=200.0, category="Salário", description="Pagamento mensal")
    assert account.balance == 200.0
    assert len(account.transactions) == 1
    assert transaction.amount == 200.0
    assert transaction.category == "Salário"
    assert transaction.description == "Pagamento mensal"

def test_get_transactions():
    account = Account(name="Conta Viagem")
    today = datetime.now()
    account.add_transaction(amount=100.0, category="Hotel", description="Reserva", date=today)
    account.add_transaction(amount=-50.0, category="Comida", description="Jantar", date=today - timedelta(days=1))

    # Sem filtros
    assert len(account.get_transactions()) == 2

    # Filtrar por data
    assert len(account.get_transactions(start_date=today - timedelta(days=2))) == 2
    assert len(account.get_transactions(start_date=today + timedelta(days=1))) == 0

    # Filtrar por categoria
    assert len(account.get_transactions(category="Hotel")) == 1

from datetime import datetime
from finances.core import Transaction

def test_transaction_initialization():
    transaction = Transaction(amount=100.0, date=datetime.now(), category="Alimentação", description="Compra no mercado")
    assert transaction.amount == 100.0
    assert transaction.category == "Alimentação"
    assert transaction.description == "Compra no mercado"
    assert isinstance(transaction.date, datetime)

def test_transaction_str_representation():
    transaction = Transaction(amount=50.0, date=datetime.now(), category="Transporte", description="Corrida de Uber")
    expected = f"Transação: Corrida de Uber R$ 50.00 (Transporte)"
    assert str(transaction) == expected

def test_transaction_update():
    transaction = Transaction(amount=100.0, date=datetime.now(), category="Saúde")
    transaction.update(amount=150.0, description="Consulta médica")
    assert transaction.amount == 150.0
    assert transaction.description == "Consulta médica"

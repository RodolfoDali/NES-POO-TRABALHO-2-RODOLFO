from finances.core import Client
from finances.core import Account
from finances.core import Investment
from datetime import datetime, timedelta

def test_client_initialization():
    client = Client(name="João")
    assert client.name == "João"
    assert len(client.accounts) == 0
    assert len(client.investments) == 0

def test_add_account():
    client = Client(name="Maria")
    account = client.add_account("Conta Corrente")
    assert len(client.accounts) == 1
    assert client.accounts[0].name == "Conta Corrente"

def test_add_investment():
    client = Client(name="Ana")
    investment = Investment(type="Ações", initial_amount=2000.0, rate_of_return=0.02)
    client.add_investment(investment)
    assert len(client.investments) == 1
    assert client.investments[0].type == "Ações"

def test_get_net_worth():
    client = Client(name="Carlos")
    account = client.add_account("Poupança")
    account.add_transaction(1000.0, "Depósito")
    investment = Investment(type="Tesouro", initial_amount=500.0, rate_of_return=0.01)
    investment.date_purchased = datetime.now() - timedelta(days=30 * 12)  # 1 ano
    client.add_investment(investment)
    assert round(client.get_net_worth(), 2) > 1500.0

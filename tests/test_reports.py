from finances.core import Client
from finances.core import Account
from finances.core import Investment
from finances.core import generate_report, future_value_report
from datetime import datetime, timedelta

def test_generate_report():
    client = Client(name="João")
    account = client.add_account("Conta Corrente")
    account.add_transaction(100.0, "Salário")
    report = generate_report(client)
    assert "Conta Corrente" in report
    assert "R$ 100.00" in report

def test_future_value_report():
    client = Client(name="João")
    investment = Investment(type="Tesouro", initial_amount=500.0, rate_of_return=0.01)
    client.add_investment(investment)
    future_date = datetime.now() + timedelta(days=365)  # 1 ano no futuro
    report = future_value_report(client, future_date)
    assert "Tesouro" in report
    assert "R$" in report

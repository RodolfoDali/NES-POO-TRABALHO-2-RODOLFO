from finances.core import Investment
from finances.core import Account
from datetime import datetime, timedelta

def test_investment_initialization():
    investment = Investment(type="Ações", initial_amount=1000.0, rate_of_return=0.01)
    assert investment.type == "Ações"
    assert investment.initial_amount == 1000.0
    assert isinstance(investment.date_purchased, datetime)
    assert investment.rate_of_return == 0.01

def test_calculate_value():
    investment = Investment(type="Tesouro", initial_amount=1000.0, rate_of_return=0.01)
    investment.date_purchased = datetime.now() - timedelta(days=30 * 12)  # 1 ano
    assert round(investment.calculate_value(), 2) == round(1000 * (1 + 0.01) ** 12, 2)

def test_sell_investment():
    account = Account(name="Conta Corrente")
    investment = Investment(type="Fundo Imobiliário", initial_amount=500.0, rate_of_return=0.02)
    investment.date_purchased = datetime.now() - timedelta(days=30 * 6)  # 6 meses
    investment.sell(account)
    assert account.balance > 500.0
    assert len(account.transactions) == 1

from datetime import datetime
from typing import List, Optional

class Transaction:
    """
    Classe para representar transações financeiras.

    Attributes:
        amount (float): Valor da transação.
        date (datetime): Data da transação.
        category (str): Identificador de uma categoria.
        description (str): Descrição da transação.
    """

    def __init__(self, amount: float, date: datetime, category: str, description: str = "") -> None:
        """
        Inicializa um objeto Transaction.

        Args:
            amount (float): Valor da transação.
            date (datetime): Data da transação.
            category (str): Categoria da transação.
            description (str): Descrição da transação.
        """
        self.amount = amount
        self.date = date
        self.category = category
        self.description = description

    def __str__(self) -> str:
        """Retorna uma descrição da transação."""
        return f"Transação: {self.description} R$ {self.amount:.2f} ({self.category})"

    def update(self, **attributes) -> None:
        """
        Atualiza um ou mais atributos da transação.

        Args:
            **attributes: Atributos a serem atualizados.
        """
        for key, value in attributes.items():
            if hasattr(self, key):
                setattr(self, key, value)


class Account:
    """
    Classe para representar contas e armazenar transações.

    Attributes:
        name (str): Nome da conta.
        balance (float): Saldo da conta.
        transactions (List[Transaction]): Lista de transações na conta.
    """

    def __init__(self, name: str) -> None:
        """
        Inicializa um objeto Account.

        Args:
            name (str): Nome da conta.
        """
        self.name = name
        self.balance = 0.0
        self.transactions: List[Transaction] = []

    def add_transaction(self, amount: float, category: str, description: str = "") -> Transaction:
        """
        Cria uma transação na conta e atualiza o saldo.

        Args:
            amount (float): Valor da transação.
            category (str): Categoria da transação.
            description (str): Descrição da transação.

        Returns:
            Transaction: A transação criada.
        """
        transaction = Transaction(amount, datetime.now(), category, description)
        self.transactions.append(transaction)
        self.balance += amount
        self.transactions.sort(key=lambda t: t.date)
        return transaction

    def get_transactions(self, start_date: Optional[datetime] = None, end_date: Optional[datetime] = None, category: Optional[str] = None) -> List[Transaction]:
        """
        Gera uma lista de transações filtradas.

        Args:
            start_date (Optional[datetime]): Data inicial para filtro.
            end_date (Optional[datetime]): Data final para filtro.
            category (Optional[str]): Categoria para filtro.

        Returns:
            List[Transaction]: Lista de transações filtradas.
        """
        filtered = self.transactions
        if start_date:
            filtered = [t for t in filtered if t.date >= start_date]
        if end_date:
            filtered = [t for t in filtered if t.date <= end_date]
        if category:
            filtered = [t for t in filtered if t.category == category]
        return filtered


class Investment:
    """
    Classe para representar investimentos.

    Attributes:
        type (str): Identificador do tipo de investimento.
        initial_amount (float): Valor inicial do investimento.
        date_purchased (datetime): Data de compra.
        rate_of_return (float): Taxa mensal de retorno.
    """

    def __init__(self, type: str, initial_amount: float, rate_of_return: float) -> None:
        """
        Inicializa um objeto Investment.

        Args:
            type (str): Tipo do investimento.
            initial_amount (float): Valor inicial do investimento.
            rate_of_return (float): Taxa de retorno mensal.
        """
        self.type = type
        self.initial_amount = initial_amount
        self.date_purchased = datetime.now()
        self.rate_of_return = rate_of_return

    def calculate_value(self) -> float:
        """
        Calcula o valor atual do investimento.

        Returns:
            float: Valor atual do investimento.
        """
        months = (datetime.now().year - self.date_purchased.year) * 12 + (datetime.now().month - self.date_purchased.month)
        return self.initial_amount * ((1 + self.rate_of_return) ** months)

    def sell(self, account: Account) -> None:
        """
        Vende o investimento e deposita o valor em uma conta.

        Args:
            account (Account): Conta para depositar o valor.
        """
        value = self.calculate_value()
        account.add_transaction(value, "Investimento", f"Venda de {self.type}")


class Client:
    """
    Classe para representar clientes.

    Attributes:
        name (str): Nome do cliente.
        accounts (List[Account]): Contas do cliente.
        investments (List[Investment]): Investimentos do cliente.
    """

    def __init__(self, name: str) -> None:
        """
        Inicializa um objeto Client.

        Args:
            name (str): Nome do cliente.
        """
        self.name = name
        self.accounts: List[Account] = []
        self.investments: List[Investment] = []

    def add_account(self, account_name: str) -> Account:
        """
        Cria uma conta para o cliente.

        Args:
            account_name (str): Nome da conta.

        Returns:
            Account: A conta criada.
        """
        account = Account(account_name)
        self.accounts.append(account)
        return account

    def add_investment(self, investment: Investment) -> None:
        """
        Adiciona um investimento para o cliente.

        Args:
            investment (Investment): O investimento a ser adicionado.
        """
        self.investments.append(investment)

    def get_net_worth(self) -> float:
        """
        Calcula o patrimônio líquido do cliente.

        Returns:
            float: O patrimônio líquido.
        """
        total_balance = sum(account.balance for account in self.accounts)
        total_investments = sum(investment.calculate_value() for investment in self.investments)
        return total_balance + total_investments


def generate_report(client: Client) -> str:
    """Gera um relatório financeiro para o cliente."""
    report = [f"Relatório financeiro para {client.name}"]
    report.append("\nContas:")
    for account in client.accounts:
        report.append(f"- {account.name}: R$ {account.balance:.2f}")
    report.append("\nInvestimentos:")
    for investment in client.investments:
        report.append(f"- {investment.type}: R$ {investment.calculate_value():.2f}")
    report.append(f"\nPatrimônio líquido: R$ {client.get_net_worth():.2f}")
    return "\n".join(report)


def future_value_report(client: Client, date: datetime) -> str:
    """Gera um relatório de projeção de rendimentos futuros."""
    report = [f"Projeção de rendimentos futuros para {client.name}"]
    for investment in client.investments:
        months = (date.year - investment.date_purchased.year) * 12 + (date.month - investment.date_purchased.month)
        future_value = investment.initial_amount * ((1 + investment.rate_of_return) ** months)
        report.append(f"- {investment.type} em {date.strftime('%d/%m/%Y')}: R$ {future_value:.2f}")
    return "\n".join(report)

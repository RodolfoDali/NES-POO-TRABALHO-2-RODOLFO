# Trabalho 2 NES POO Rodolfo
 
Personal Finance Manager

Um aplicativo de finanças pessoais para gerenciar receitas, despesas e investimentos. Este projeto inclui funcionalidades para rastreamento de transações, categorização, relatórios financeiros e projeções futuras.


Funcionalidades

Gerenciamento de transações financeiras (receitas e despesas).
Categorização de transações para fácil análise.
Registro e gerenciamento de investimentos com cálculo de retornos.
Relatórios financeiros detalhados para monitorar contas e patrimônio líquido.
Projeções futuras de rendimentos.
Estrutura extensível para múltiplas contas e usuários.


Tecnologias Utilizadas

Linguagem: Python 3.11.9
Bibliotecas:
pytest para testes.
datetime e outras bibliotecas padrão do Python.


Estrutura do Projeto

bash
Copiar código
projeto/
├── finances/
│   ├── __init__.py
│   ├── core.py          # Contém todas as classes principais (Transaction, Account, Investment, Client)
│   └── reports.py       # Funções para relatórios financeiros
├── tests/               # Testes automatizados com Pytest
│   ├── test_transaction.py
│   ├── test_account.py
│   ├── test_investment.py
│   ├── test_client.py
│   └── test_reports.py
├── README.md            # Este arquivo
├── requirements.txt     # Dependências do projeto
├── relations.txt        # Relações entre classes
├── setup.py             # Arquivo para instalar o pacote
└── LICENSE              # Licença do projeto


Instalação e Uso
Clone o repositório:

bash
Copiar código
git clone https://github.com/seu-usuario/personal-finance-manager.git
cd personal-finance-manager
Crie e ative um ambiente virtual:

bash
Copiar código
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate   # Windows
Instale as dependências:

bash
Copiar código
pip install -r requirements.txt
Execute os testes para validar o funcionamento:

bash
Copiar código
pytest tests/
Exemplo de uso:

No diretório do projeto, crie um arquivo example.py com o seguinte conteúdo:

python
Copiar código
from finances.core import Client

# Criando um cliente
cliente = Client("João")
conta = cliente.add_account("Conta Corrente")
conta.add_transaction(1000, "Salário", "Recebimento de salário")
print(cliente.get_net_worth())
Execute:

bash
Copiar código
python example.py

📝 Contribuindo
Contribuições são bem-vindas! Para contribuir, siga os passos:

Faça um fork do projeto.

Crie uma nova branch:

bash
Copiar código
git checkout -b minha-contribuicao
Envie suas alterações:

bash
Copiar código
git push origin minha-contribuicao
Abra um pull request.


Licença

Este projeto está licenciado sob a MIT License. Veja o arquivo LICENSE para mais detalhes.


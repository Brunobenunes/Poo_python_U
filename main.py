''' Crição simples de um sistema Bancário'''

from abc import ABC, abstractmethod


class Person(ABC):
    ''' Classe pessoa, contendo informaçes sobre a pessoa'''
    def __init__(self, name, cpf, age, address):
        super().__init__()
        self.name = name
        self.cpf = cpf
        self.age = age
        self.address = address



class Client(Person):
    '''Classe Client, herdando dados da Pessoa'''
    def __init__(self, name, cpf, age, address):
        super().__init__(name, cpf, age, address)
        self.accounts = []


class Account(ABC):
    ''' Classe Account, possui dados da conta'''
    def __init__(self, number_, balance) -> None:
        super().__init__()
        self.number = number_
        self.balance = balance


    def deposit(self, value):
        ''' Metodo para depoistar um determinado valor na conta'''
        self.balance += value

    @abstractmethod
    def withdraw(self, value):
        ''' Metodo abstrado para sacar um determinado valor da conta'''
        self.balance -= value


class CheckingAccount(Account):
    ''' Classe CheckingAccount, herda dados de Account e possui atributos especiais'''
    def __init__(self, number_, balance) -> None:
        super().__init__(number_, balance)
        self.limit = -500


    def withdraw(self, value):
        self.balance -= value


class SavingAccount(Account):
    ''' Classe Saving Account, herda dados de Account e possui atributos especias'''
    def __init__(self, number_, balance) -> None:
        super().__init__(number_, balance)
        self.limit = 0


    def withdraw(self, value):
        self.balance -= value


class Bank:
    ''' Classe Bank, possui dados relacionado ao banco, como clients e contas cadastradas'''
    def __init__(self, name) -> None:
        self.accounts = []
        self.clients = []
        self.branchs = []
        self.name = name

    def verify_account(self, account):
        ''' Metodo que verifica se uma conta é do banco'''
        return account in self.accounts

    def verify_client(self, client_cpf):
        ''' Metodo que verifica se o cliente é do banco'''
        return client_cpf in self.clients

    def verify_branch(self, branch):
        ''' Metodo que verifica se a agencia é do banco'''
        return branch in self.branchs
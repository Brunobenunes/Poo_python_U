''' Crição simples de um sistema Bancário'''

from abc import ABC, abstractmethod

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

    def add_client(self, client):
        ''' Adcionando o client especificado a lista de accounts'''
        if self.verify_client(client.cpf):
            print(f'@@@@ O cliente com o CPF : {client.cpf} já Existe! @@@@')





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

    @classmethod
    def create(cls, bank : Bank):
        ''' Metodo para cirar um novo cliente e adicionar ao Banco especificado'''
        name = input('Digite seu nome e sobrenome: ')
        cpf = input('Digite seu CPF sem pontuação: ')
        age = input('Digite sua Idade: ')
        street = input('Digite a rua/av e o número da casa/complemento: ').title()
        district = input('Digite o seu Bairro: ')
        state = input('Digite o UF: *MG*').upper()
        address = f"{street} - {district}/{state}"
        new_client = cls(name=name, cpf=cpf, age=age, address=address)
        bank.add_client(new_client)
        return new_client




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

def login_menu(bank : Bank):
    ''' Menu De Login do Banco informado '''
    while True:
        menu_display = f'''
    _______________________________________________________
            $$$ Bem vindo ao Banco {bank.name} $$$

        [e] Entrar
        [c] Cadastrar
        [q] Sair

    _______________________________________________________

    '''
        command = input(menu_display).lower()

        if command == 'q':
            print('################# Tenha Um Ótimo Dia! #################')

        if command == 'c':
            Client.create(Bank)
            continue

        if command == 'e':
            login_cpf = input('Digite seu CPF: ')

            if bank.verify_client(login_cpf):
                # todo client_menu()
                break # Retirar após client_menu() estiver pronto

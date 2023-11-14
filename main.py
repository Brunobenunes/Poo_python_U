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
        for client in self.clients:
            if client.cpf == client_cpf:
                return client
        return False

    def verify_branch(self, branch):
        ''' Metodo que verifica se a agencia é do banco'''
        return branch in self.branchs

    def add_client(self, client):
        ''' Adcionando o client especificado a lista de clients'''
        if self.verify_client(client.cpf):
            print(f'@@@@ O cliente com o CPF : {client.cpf} já Existe! @@@@')
        else:
            self.clients.append(client)
    
    def account_add(self, account):
        ''' Adcionando a conta especificada a lista de accounts'''
        self.accounts.append(account.number)






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
    def __init__(self, name, cpf, age, address, bank):
        super().__init__(name, cpf, age, address)
        self.accounts = []
        self.bank = bank

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
        new_client = cls(name=name, cpf=cpf, age=age, address=address, bank=bank)
        bank.add_client(new_client)
        return new_client




class Account(ABC):
    ''' Classe Account, possui dados da conta'''
    def __init__(self, number_, balance = 0) -> None:
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

    @classmethod
    @abstractmethod
    def create(cls, client: Client):
        ''' Criando instacia de uma Conta'''


class CheckingAccount(Account):
    ''' Classe CheckingAccount, herda dados de Account e possui atributos especiais'''
    def __init__(self, number_, balance=0) -> None:
        super().__init__(number_, balance)
        self.limit = -500


    def withdraw(self, value):
        self.balance -= value

    @classmethod
    def create(cls, client : Client):
        ''' Criando uma instacia de Conta-Corrente'''
        account_number = len(client.bank.accounts)
        new_account = cls(account_number)
        client.bank.account_add(new_account)
        client.accounts.append(new_account.number)
        return new_account



class SavingAccount(Account):
    ''' Classe Saving Account, herda dados de Account e possui atributos especias'''
    def __init__(self, number_, balance=0) -> None:
        super().__init__(number_, balance)
        self.limit = 0


    def withdraw(self, value):
        self.balance -= value

    @classmethod
    def create(cls, client: Client):
        ''' Criando uma instacia de Conta Poupança'''
        account_number = len(client.bank.accounts)
        new_account = cls(account_number)
        client.bank.account_add(new_account)
        client.accounts.append(new_account.number)
        return new_account



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
            break

        if command == 'c':
            Client.create(bank)
            continue

        if command == 'e':
            login_cpf = input('Digite seu CPF: ')
            client = bank.verify_client(login_cpf)

            if client:
                client_menu(client)
            else: print(f'@@@@ Cliente com o CPF: {login_cpf} NÂO ENCONTRADO! @@@@')

                


def client_menu(client : Client):
    ''' Menu do Cliente após Login'''
    while True:
        menu_display = f'''
        _______________________________________________________
                $$$ Bem Vindo(a) {client.name} $$$

            [l] Listar Contas
            [a] Acessar Conta
            [c] Criar Conta
            [q] Sair

        _______________________________________________________

        '''
        command = input(menu_display)

        if command == 'q':
            print('################# Tenha Um Ótimo Dia! #################')
            break

        elif command == 'l':
            if client.accounts:
                print('_____ Suas Contas Cadastradas:')
                for acc in client.accounts:
                    print(acc)
                print()
                continue
            else:
                print('@@@@ Você ainda não possui contas cadastradas @@@@')
                continue
        elif command == 'c':
            account_type = input('''
_______________________________________________________
            Qual Tipo de Conta deseja Criar?
                                 
    [c] Conta-Corrente
    [p] Conta Poupança
    [q] Sair

_______________________________________________________
''')
            if account_type == 'q':
                continue
            elif account_type == 'c':
                CheckingAccount.create(client)
            elif account_type == 'p':
                SavingAccount.create(client)
            else:
                print('@@@@ Comando Inválido! Tente Novamente @@@@')
                continue

        elif command == 'a':
            print('''
_______________________________________________________
    Digite o Número da Conta que deseja acessar:''')
            for acc in client.accounts:
                print(acc)
            print('_______________________________________________________')
            account_choice = input('\nConta Escolhida: ')
            #account_menu()
            print(f'Acessando Conta: {account_choice}')
            break

        else:
            print('@@@@ Comando Inválido! Tente Novamente @@@@')
            continue





dio_Bank = Bank('DiO')

login_menu(dio_Bank)

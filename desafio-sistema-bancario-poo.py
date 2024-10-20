#desafio do sistema bancário bootcamp DIO - atualizando o sistema com programação orientada objeto, 
#incluindo classes, métodos, heranças, classes abstratas, polimorfismo, entre outros

from datetime import date, datetime, timedelta
from abc import ABC, abstractmethod, abstractproperty

class Cliente:
    def __init__(self, endereco):
        self._endereco = endereco
        self._contas = []

    def realizar_transação(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, endereco, contas, cpf, nome, data_nascimento):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()
        
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property    
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    def sacar(self, valor):
        saldo = self._saldo
        saldo_excedido = valor > saldo
        if saldo_excedido:
            print("\nFalha na operação: você não pode sacar um valor maior que o seu saldo.") 
        elif valor > 0:
            self._saldo -= valor
            print(f"\nSaque de R${valor:.2f} concluído com sucesso.")
            return True
        else:
            print("Falha na operação: valor inválido, tente novamente.")  

        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"\nDepósito de R${valor:.2f} concluído com sucesso.")
        else:
            print("Valor inválido, tente novamente.") 
            return False
        
        return True

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite = 500, limite_saques = 3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques
    
    def sacar(self, valor): #sobrescrita do método sacar para abranger restrições do exercício
        numero_saques = len([transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__])
        limite_excedido = valor > self.limite 
        saques_excedidos = numero_saques >= self.limite_saques

        if limite_excedido:
            print("\nFalha na operação: você não pode sacar um valor maior que o seu limite por transação.")
        elif saques_excedidos:
            print("\nFalha na operação: você já atingiu o limite de saques diário.")
        else:
            return super().sacar(valor) #chamando o sacar da classe pai
        
        return False
    
    def __str__(self):
        return f"""
            Agência:\t{self.agencia}
            Conta corrente:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
            }
        )
        return None

class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractmethod
    def registrar(self,conta):
        pass

class Deposito(Transacao):
    def __init__(self,valor):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        transacao_sucedida = conta.depositar(self.valor)
        if transacao_sucedida:
            conta.historico.adicionar_transacao(self)

class Saque(Transacao):
    def __init__(self,valor):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        transacao_sucedida = conta.sacar(self.valor)
        if transacao_sucedida:
            conta.historico.adicionar_transacao(self)
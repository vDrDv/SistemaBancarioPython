class Banco:
    def __init__(self):
        self.saldo = 0
        self.depositos = []
        self.saques = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.depositos.append(valor)
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if self.saldo >= valor and (sum(self.saques) + valor) <= 500 and len(self.saques) < 3 and valor <= 500:
            self.saldo -= valor
            self.saques.append(valor)
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        elif (sum(self.saques) + valor) > 500:
            print("Limite diário de saques de R$ 500 atingido.")
        elif len(self.saques) >= 3:
            print("Limite máximo de saques diários atingido.")
        else:
            print("Saldo insuficiente ou valor de saque inválido.")

    def extrato(self):
        print("Extrato:")
        if not self.depositos and not self.saques:
            print("Não foram realizadas movimentações.")
        else:
            for deposito in self.depositos:
                print(f"Depósito: R$ {deposito:.2f}")
            for saque in self.saques:
                print(f"Saque: R$ {saque:.2f}")
            print(f"Saldo atual: R$ {self.saldo:.2f}")


# Criar uma instância do banco
banco = Banco()

# Simular operações com input do usuário
while True:
    print("\nEscolha uma operação:")
    print("1 - Depósito")
    print("2 - Saque")
    print("3 - Extrato")
    print("4 - Sair")
    
    opcao = input("Opção: ")
    
    if opcao == "1":
        valor = float(input("Digite o valor do depósito: "))
        banco.depositar(valor)
    elif opcao == "2":
        valor = float(input("Digite o valor do saque: "))
        banco.sacar(valor)
    elif opcao == "3":
        banco.extrato()
    elif opcao == "4":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida. Digite novamente.")

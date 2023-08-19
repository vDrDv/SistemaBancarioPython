class Banco:
    def __init__(self):
        self.usuarios = {}

    def cadastrar_usuario(self, nome, cpf):
        self.usuarios[cpf] = {'nome': nome, 'contas': {}}
        print(f"Usuário {nome} cadastrado com sucesso.")

    def cadastrar_conta_bancaria(self, cpf, numero_conta):
        if cpf in self.usuarios:
            if numero_conta not in self.usuarios[cpf]['contas']:
                self.usuarios[cpf]['contas'][numero_conta] = {'saldo': 0, 'depositos': [], 'saques': []}
                print(f"Conta bancária número {numero_conta} cadastrada para o usuário {self.usuarios[cpf]['nome']}.")
            else:
                print("Número de conta já cadastrado para este usuário.")
        else:
            print("Usuário não encontrado.")

    def depositar(self, cpf, numero_conta, valor):
        if cpf in self.usuarios and numero_conta in self.usuarios[cpf]['contas'] and valor > 0:
            self.usuarios[cpf]['contas'][numero_conta]['saldo'] += valor
            self.usuarios[cpf]['contas'][numero_conta]['depositos'].append(valor)
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        elif cpf in self.usuarios and numero_conta in self.usuarios[cpf]['contas']:
            print("Valor de depósito inválido.")
        else:
            print("Usuário não encontrado ou número de conta inválido.")

    def sacar(self, cpf, numero_conta, valor):
        if cpf in self.usuarios and numero_conta in self.usuarios[cpf]['contas'] and self.usuarios[cpf]['contas'][numero_conta]['saldo'] >= valor and (sum(self.usuarios[cpf]['contas'][numero_conta]['saques']) + valor) <= 500 and len(self.usuarios[cpf]['contas'][numero_conta]['saques']) < 3 and valor <= 500:
            self.usuarios[cpf]['contas'][numero_conta]['saldo'] -= valor
            self.usuarios[cpf]['contas'][numero_conta]['saques'].append(valor)
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        elif cpf in self.usuarios and numero_conta in self.usuarios[cpf]['contas'] and (sum(self.usuarios[cpf]['contas'][numero_conta]['saques']) + valor) > 500:
            print("Limite diário de saques de R$ 500 atingido.")
        elif cpf in self.usuarios and numero_conta in self.usuarios[cpf]['contas'] and len(self.usuarios[cpf]['contas'][numero_conta]['saques']) >= 3:
            print("Limite máximo de saques diários atingido.")
        else:
            print("Usuário não encontrado, número de conta inválido, saldo insuficiente ou valor de saque inválido.")

    def extrato(self, cpf, numero_conta):
        if cpf in self.usuarios and numero_conta in self.usuarios[cpf]['contas']:
            print(f"Extrato da Conta {numero_conta} do usuário {self.usuarios[cpf]['nome']}:")
            for deposito in self.usuarios[cpf]['contas'][numero_conta]['depositos']:
                print(f"Depósito: R$ {deposito:.2f}")
            for saque in self.usuarios[cpf]['contas'][numero_conta]['saques']:
                print(f"Saque: R$ {saque:.2f}")
            print(f"Saldo atual: R$ {self.usuarios[cpf]['contas'][numero_conta]['saldo']:.2f}")
        else:
            print("Usuário não encontrado ou número de conta inválido.")

# Criar uma instância do banco
banco = Banco()

# Simular operações com input do usuário
while True:
    print("\nEscolha uma operação:")
    print("1 - Cadastrar Usuário")
    print("2 - Cadastrar Conta Bancária")
    print("3 - Depósito")
    print("4 - Saque")
    print("5 - Extrato")
    print("6 - Sair")
    
    opcao = input("Opção: ")
    
    if opcao == "1":
        nome = input("Digite o nome do usuário: ")
        cpf = input("Digite o CPF do usuário: ")
        banco.cadastrar_usuario(nome, cpf)
    elif opcao == "2":
        cpf = input("Digite o CPF do usuário: ")
        numero_conta = input("Digite o número da conta bancária: ")
        banco.cadastrar_conta_bancaria(cpf, numero_conta)
    elif opcao == "3":
        cpf = input("Digite o CPF do usuário: ")
        numero_conta = input("Digite o número da conta bancária: ")
        valor = float(input("Digite o valor do depósito: "))
        banco.depositar(cpf, numero_conta, valor)
    elif opcao == "4":
        cpf = input("Digite o CPF do usuário: ")
        numero_conta = input("Digite o número da conta bancária: ")
        valor = float(input("Digite o valor do saque: "))
        banco.sacar(cpf, numero_conta, valor)
    elif opcao == "5":
        cpf = input("Digite o CPF do usuário: ")
        numero_conta = input("Digite o número da conta bancária: ")
        banco.extrato(cpf, numero_conta)
    elif opcao == "6":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida. Digite novamente.")

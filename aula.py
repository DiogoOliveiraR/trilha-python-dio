class ContaCorrente:
    def __init__(self, titular, numero_conta):
        self.titular = titular
        self.numero_conta = numero_conta
        self.saldo = 0.0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Erro: Valor de depósito inválido. O valor deve ser maior que zero.")

    def sacar(self, valor):
        if valor <= 0:
            print("Erro: Valor de saque inválido. O valor deve ser maior que zero.")
        elif valor > self.saldo:
            print("Erro: Saldo insuficiente.")
        else:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")

    def extrato(self):
        print(f"Extrato da conta {self.numero_conta} - Titular: {self.titular}")
        print(f"Saldo atual: R${self.saldo:.2f}")

    def consultar_saldo(self):
        print(f"Saldo atual de {self.titular} (Conta {self.numero_conta}): R${self.saldo:.2f}")

def obter_valor(valor_tipo):
    while True:
        try:
            valor = float(input(f"Digite o valor para {valor_tipo}: R$"))
            if valor > 0:
                return valor
            else:
                print("Erro: O valor deve ser maior que zero. Tente novamente.")
        except ValueError:
            print("Erro: Entrada inválida. Por favor, insira um número válido.")

def criar_novo_usuario():
    print("\nCriar novo usuário:")
    nome = input("Digite o nome do titular: ")
    numero_conta = input("Digite o número da conta: ")
    
    # Verificar se o número da conta é um valor válido
    while not numero_conta.isdigit():
        print("Erro: O número da conta deve ser composto apenas por dígitos.")
        numero_conta = input("Digite o número da conta: ")

    numero_conta = int(numero_conta)  # Converter para inteiro
    nova_conta = ContaCorrente(nome, numero_conta)
    print(f"Conta criada com sucesso! Titular: {nome}, Número da conta: {numero_conta}")
    return nova_conta

def listar_contas(contas):
    if contas:
        print("\nListando todas as contas:")
        for conta in contas.values():
            print(f"Conta {conta.numero_conta} - Titular: {conta.titular} - Saldo: R${conta.saldo:.2f}")
    else:
        print("Não há contas cadastradas.")

def main():
    print("Bem-vindo ao Sistema Bancário!\n")

    contas = {}  # Dicionário para armazenar as contas dos usuários
    
    while True:
        print("\nSelecione uma operação:")
        print("[d] - Depositar")
        print("[s] - Sacar")
        print("[e] - Extrato")
        print("[nc] - Nova Conta")
        print("[lc] - Listar Contas")
        print("[nu] - Novo Usuário")
        print("[q] - Sair")

        opcao = input("Digite o número da operação desejada: ").lower()

        if opcao == "d":
            numero_conta = int(input("Digite o número da conta para depósito: "))
            if numero_conta in contas:
                valor = obter_valor("depósito")
                contas[numero_conta].depositar(valor)
                contas[numero_conta].consultar_saldo()
            else:
                print("Erro: Conta não encontrada.")
        elif opcao == "s":
            numero_conta = int(input("Digite o número da conta para saque: "))
            if numero_conta in contas:
                valor = obter_valor("saque")
                contas[numero_conta].sacar(valor)
                contas[numero_conta].consultar_saldo()
            else:
                print("Erro: Conta não encontrada.")
        elif opcao == "e":
            numero_conta = int(input("Digite o número da conta para extrato: "))
            if numero_conta in contas:
                contas[numero_conta].extrato()
            else:
                print("Erro: Conta não encontrada.")
        elif opcao == "nc":
            nova_conta = criar_novo_usuario()
            contas[nova_conta.numero_conta] = nova_conta
        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "nu":
            nova_conta = criar_novo_usuario()
            contas[nova_conta.numero_conta] = nova_conta
        elif opcao == "q":
            print("Saindo... Até logo!")
            break
        else:
            print("Erro: Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

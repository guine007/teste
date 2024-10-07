class Cliente:
    def __init__(self, nome, sobrenome, idade, sexo, email, cidade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.sexo = sexo
        self.email = email
        self.cidade = cidade

    def __str__(self):
        return f'Nome: {self.nome} {self.sobrenome}, Idade: {self.idade}, Sexo: {self.sexo}, Email: {self.email}, Cidade: {self.cidade}'

def cadastrar_cliente():
    nome = input('Nome: ')
    sobrenome = input('Sobrenome: ')
    idade = input('Idade: ')
    sexo = input('Sexo: ')
    email = input('Email: ')
    cidade = input('Cidade: ')
    return Cliente(nome, sobrenome, idade, sexo, email, cidade)

def exibir_clientes(clientes):
    for cliente in clientes:
        print(cliente)

def main():
    clientes = []
    while True:
        print("1. Cadastrar cliente")
        print("2. Exibir todos os clientes")
        print("3. Sair")
        opcao = input('Escolha uma opção: ')
        if opcao == '1':
            cliente = cadastrar_cliente()
            clientes.append(cliente)
        elif opcao == '2':
            exibir_clientes(clientes)
        elif opcao == '3':
            break
        else:
            print('Opção inválida!')

if __name__ == "__main__":
    main()

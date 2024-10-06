# Função para coletar dados dos alunos
def coletar_dados():
    alunos = []
    while True:
        nome = input("Digite o nome do aluno (ou 'sair' para finalizar): ")
        if nome.lower() == 'sair':
            break
        sobrenome = input("Digite o sobrenome do aluno: ")
        nota = float(input("Digite a nota do aluno: "))
        alunos.append({'nome': nome, 'sobrenome': sobrenome, 'nota': nota})
    return alunos

# Função para exibir os dados dos alunos
def exibir_dados(alunos):
    for aluno in alunos:
        print(f"Nome: {aluno['nome']} {aluno['sobrenome']}, Nota: {aluno['nota']}")

# Função principal
def main():
    alunos = coletar_dados()
    exibir_dados(alunos)

if __name__ == "__main__":
    main()
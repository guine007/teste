# for item in sequence:

print("*** strings ***")
palavra = 'python'
for letra in palavra:
    print(letra)

    print("*** listas ***")
    lista = ["python", "java", "c#"]
    for linguagem in lista:
        print(linguagem)

        print("*** Dicionarios ***")
        dicionarios = {"linguagem": "python","versão": 3.20, "biblioteca": "pandas"}
        for chave in dicionarios:
            print(f"{chave}:{dicionarios[chave]}")
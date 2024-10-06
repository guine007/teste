# dados for
dados = ["nome", "sobrenome","idade", "sexo","e-meil"]
for dados in dados:
    print(dados)
 # dados while 
    contador = 0
    while contador < 5 :
        print(contador)
        contador +=1
        # dados break 

        contador = 0
        while True:
            print(contador)
            contador +=2
            if contador == 10:
                break

            # dados continue 
            for i in range(10):
                if i % 2 == 0:
                    continue
                print(i)

                # dados pass

                for i in range(5):
                    pass
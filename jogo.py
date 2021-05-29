from limpadorDeTela import limpartela, linhavazia, delay

contadorPartidas = 1
while True:
    limpartela()
    arquivo = open('registros.txt', 'r')
    arquivo.read()
    arquivo.close()
    arquivo= open('registros.txt', 'a')

    arquivo.write(" Histórico da partida número: " + str(contadorPartidas)+ '\n')

    nomeDesafiante = input('Qual o nome do desafiante? ')
    linhavazia()
    nomeCompetidor = input('Qual o nome do competidor? ')

    limpartela()
    palavraChave = input('Qual a palavra chave? ')
    if any(chr.isdigit() for chr in palavraChave):
        print("\n Digite uma palavra e não um número! ")
        delay()
    else:
        arquivo.write("\n A palavra chave é: " +palavraChave)
        if palavraChave != '':
            linhavazia()
            dica1 = input('Qual a primeira dica? ')
            linhavazia()
            dica2 = input('Qual a segunda dica? ')
            linhavazia()
            dica3 = input('Qual a terceira dica? ')
            limpartela()
            if contadorPartidas > 1:
                arquivo.write('\n')
            arquivo.write(" Nome do desafiante: " +nomeDesafiante)
            arquivo.write("\n Nome do competidor: " +nomeCompetidor)
            limpartela()

            
            digitadas = []

            valorPalavraChave = len(palavraChave)
            contador =0 
            while contador < valorPalavraChave:
                contador += 1

            valorAsteriscos = '*' * contador
            print(f' A palavra contém {contador} letras\n\n Essa é a palavra: {valorAsteriscos}\n')

            linhavazia()
            jogar= 'jogar'
            dica = 'dica'
            chances = 5
            contadorDica1 = 0
            contadorDica2 = 0
            contadorDica3 = 0
            jogar_novamente = "jogar novamente"
            sair_do_jogo = "sair do jogo"


            linhavazia()
            secreto_temporario = ''
            while palavraChave != secreto_temporario:
                escolha = input(' Deseja jogar ou pedir uma dica? ')
                linhavazia()
                if jogar in escolha:
                    letra = input(' Qual letra você deseja jogar? ')
                    linhavazia()
                    digitadas.append(letra)
                    if letra in palavraChave:
                        print(f' A letra {letra}, existe na palavra!\n ')
                        linhavazia()
                    else:
                        print(f' A letra {letra} não existe na palavra!\n ')
                        linhavazia()
                        digitadas.pop()
                    secreto_temporario = ''
                    for letra_secreta in palavraChave:
                        if letra_secreta in digitadas:
                            secreto_temporario += letra_secreta
                        else:
                            secreto_temporario += '*'

                    if secreto_temporario == palavraChave:
                            print(f' Parabéns você ganhou, a palavra era {palavraChave}')
                            contadorPartidas += 1
                            arquivo.write("\n Vencedor: " +nomeCompetidor)
                            arquivo.write("\n Desafiante: " +nomeDesafiante+ '\n\n')
                            linhavazia()
                            arquivo.close()
                            arquivo = open('registros.txt', 'r')
                            conteudo = arquivo.read()
                            arquivo.close()
                            arquivo= open('registros.txt', 'a')
                            print(conteudo)
                            sair_ou_entrar = input(' Deseja jogar novamente ou sair do jogo? ')
                            if sair_do_jogo in sair_ou_entrar:
                                quit()
                    else:
                            print(f' A palavra secreta está assim: {secreto_temporario}\n')
                            linhavazia()
                    if letra not in palavraChave:
                            chances -= 1
                            print(f' Você ainda tem {chances} chances\n')
                            linhavazia()
                            if chances == 0:
                                print(' Você perdeu! ')
                                contadorPartidas += 1
                                arquivo.write("\n Vencedor: " +nomeDesafiante)
                                arquivo.write("\n Competidor: " +nomeCompetidor+ '\n\n')
                                linhavazia()
                                arquivo.close()
                                arquivo = open('registros.txt', 'r')
                                conteudo = arquivo.read()
                                arquivo.close()
                                arquivo= open('registros.txt', 'a')
                                print(conteudo)
                                sair_ou_entrar = input(' Deseja jogar novamente ou sair do jogo? ')
                elif dica in escolha:
                    if contadorDica1 < 1:
                        dica in escolha
                        linhavazia()
                        print(' A dica é:', dica1,'\n')
                        contadorDica1 += 1
                        
                    elif contadorDica2 < 1:
                        dica in escolha
                        linhavazia()
                        print(' A dica é:',dica2,'\n')
                        contadorDica2 += 1
                        
                    elif contadorDica3 < 1:
                        dica in escolha
                        linhavazia()
                        print(' A dica é:',dica3,'\n')
                        contadorDica3 += 1
                        
                    elif contadorDica1 == 1 and contadorDica2 == 1 and contadorDica3 == 1:
                        linhavazia()
                        print(' As dicas acabaram!\n ')
            arquivo.close()
        else:
            print('Digite uma palavra correta!! ')
            delay()

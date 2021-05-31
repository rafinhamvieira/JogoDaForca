from functionBasic import cleanerScreen, emptyLine, delay

counterMatches = 1
while True:
    cleanerScreen()
    archive = open('records.txt', 'r')
    archive.read()
    archive.close()
    archive= open('records.txt', 'a')

    archive.write(" Histórico da partida número: " + str(counterMatches)+ '\n')

    challengingName = input('Qual o nome do desafiante? ')
    emptyLine()
    competitorName = input('Qual o nome do competidor? ')

    cleanerScreen()
    keyWord = input('Qual a palavra chave? ')
    if any(chr.isdigit() for chr in keyWord):
        print("\n Digite uma palavra e não um número! ")
        delay()
    else:
        archive.write("\n A palavra chave é: " +keyWord)
        if keyWord != '':
            emptyLine()
            tip1 = input('Qual a primeira dica? ')
            emptyLine()
            tip2 = input('Qual a segunda dica? ')
            emptyLine()
            tip3 = input('Qual a terceira dica? ')
            cleanerScreen()
            if counterMatches > 1:
                archive.write('\n')
            archive.write(" Nome do desafiante: " +challengingName)
            archive.write("\n Nome do competidor: " +competitorName)
            cleanerScreen()

            
            typed = []

            valuekeyWord = len(keyWord)
            counter =0 
            while counter < valuekeyWord:
                counter += 1

            asterisksValue = '*' * counter
            print(f' A palavra contém {counter} words\n\n Essa é a palavra: {asterisksValue}\n')

            emptyLine()
            play = 'jogar'
            tip = 'dica'
            chances = 5
            tipCounter1 = 0
            tipCounter2 = 0
            tipCounter3 = 0
            playAgain = "jogar novamente"
            quitGame = "sair do jogo"


            emptyLine()
            temporarySecret = ''
            while keyWord != temporarySecret:
                choice = input(' Deseja jogar ou pedir uma dica? ')
                emptyLine()
                if play in choice:
                    word = input(' Qual word você deseja jogar? ')
                    emptyLine()
                    typed.append(word)
                    if word in keyWord:
                        print(f' A word {word}, existe na palavra!\n ')
                        emptyLine()
                    else:
                        print(f' A word {word} não existe na palavra!\n ')
                        emptyLine()
                        typed.pop()
                    temporarySecret = ''
                    for secretWord in keyWord:
                        if secretWord in typed:
                            temporarySecret += secretWord
                        else:
                            temporarySecret += '*'

                    if temporarySecret == keyWord:
                            print(f' Parabéns você ganhou, a palavra era {keyWord}')
                            counterMatches += 1
                            archive.write("\n Vencedor: " +competitorName)
                            archive.write("\n Desafiante: " +challengingName+ '\n\n')
                            emptyLine()
                            archive.close()
                            archive = open('records.txt', 'r')
                            contents = archive.read()
                            archive.close()
                            archive= open('records.txt', 'a')
                            print(contents)
                            quitOrPlay = input(' Deseja jogar novamente ou sair do jogo? ')
                            if quitGame in quitOrPlay:
                                quit()
                    else:
                            print(f' A palavra secreta está assim: {temporarySecret}\n')
                            emptyLine()
                    if word not in keyWord:
                            chances -= 1
                            print(f' Você ainda tem {chances} chances\n')
                            emptyLine()
                            if chances == 0:
                                print(' Você perdeu! ')
                                counterMatches += 1
                                archive.write("\n Vencedor: " +challengingName)
                                archive.write("\n Competidor: " +competitorName+ '\n\n')
                                emptyLine()
                                archive.close()
                                archive = open('records.txt', 'r')
                                contents = archive.read()
                                archive.close()
                                archive= open('records.txt', 'a')
                                print(contents)
                                quitOrPlay = input(' Deseja jogar novamente ou sair do jogo? ')
                elif tip in choice:
                    if tipCounter1 < 1:
                        tip in choice
                        emptyLine()
                        print(' A dica é:', tip1,'\n')
                        tipCounter1 += 1
                        
                    elif tipCounter2 < 1:
                        tip in choice
                        emptyLine()
                        print(' A dica é:',tip2,'\n')
                        tipCounter2 += 1
                        
                    elif tipCounter3 < 1:
                        tip in choice
                        emptyLine()
                        print(' A dica é:',tip3,'\n')
                        tipCounter3 += 1
                        
                    elif tipCounter1 == 1 and tipCounter2 == 1 and tipCounter3 == 1:
                        emptyLine()
                        print(' As dicas acabaram!\n ')
            archive.close()
        else:
            print('Digite uma palavra correta!! ')
            delay()

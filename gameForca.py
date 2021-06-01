from functionBasic import cleanerScreen, emptyLine, delay

counterMatches = 1
while True:
    cleanerScreen()
    archive = open('records.txt', 'r')
    archive.read()
    archive.close()
    archive= open('records.txt', 'a')

    challengingName = input(' Qual o nome do desafiante? ')
    emptyLine()
    competitorName = input(' Qual o nome do competidor? ')

    cleanerScreen()
    while True:    
        keyWord = input(' Qual é a palavra chave? ')
        numberKeyWord = len(keyWord)    
        if any(chr.isdigit() for chr in keyWord):
            print("\n Digite uma palavra e não um número! ")
            delay()
            cleanerScreen()
        elif numberKeyWord == 1:
            print("\n Digite mais de uma letra! ")
            delay()
            cleanerScreen()
        elif numberKeyWord == 0:
            print('\n Digite uma palavra correta!! ')
            delay()
            cleanerScreen()
        else:
            archive.write("\n Histórico da partida número: " + str(counterMatches)+ '\n')
            archive.write("\n A palavra chave é: " +keyWord)
            if keyWord != '':
                emptyLine()
                tip1 = input(' Qual a primeira dica? ')
                emptyLine()
                tip2 = input(' Qual a segunda dica? ')
                emptyLine()
                tip3 = input(' Qual a terceira dica? ')
                cleanerScreen()
                
                archive.write("\n Nome do desafiante: " +challengingName)
                archive.write("\n Nome do competidor: " +competitorName)
                cleanerScreen()
                
                play = 'jogar'
                tip = 'dica'
                chances = 5
                tipCounter1 = 0
                tipCounter2 = 0
                tipCounter3 = 0
                playAgain = "jogar novamente"
                quitGame = "sair do jogo"
                typed = []
                wordList = []

                valuekeyWord = len(keyWord)
                counter =0 
                while counter < valuekeyWord:
                    counter += 1
                asterisksValue = '*' * counter
                print(f' A palavra contém {counter} letras\n\n Essa é a palavra: {asterisksValue}\n')
                temporarySecret = ''
                while keyWord != temporarySecret:
                    choice = input(' Deseja jogar ou pedir uma dica? ')
                    emptyLine()
                    while True:
                        if tip in choice:
                            if tipCounter1 < 1:
                                tip in choice
                                print(' A dica é:', tip1,'\n')
                                tipCounter1 = 1
                                choice = 'jogar'
                            elif tipCounter2 < 1:
                                tip in choice
                                emptyLine()
                                print(' A dica é:',tip2,'\n')
                                tipCounter2 = 1
                                choice = 'jogar'
                            elif tipCounter3 < 1:
                                tip in choice
                                emptyLine()
                                tipCounter3 = 1
                                print(' A dica é:',tip3,'\n')
                                choice = 'jogar'
                            elif tipCounter1 == 1 and tipCounter2 == 1 and tipCounter3 == 1:
                                emptyLine()
                                print(' As dicas acabaram!\n ')
                                choice = 'jogar'
                        if play in choice:
                            wordList = []
                            word = input(' Qual letra você deseja jogar? ')
                            for element in word:
                                wordList.append(element)
                            while len(wordList) > 1 :
                                print('\n Você só pode colocar uma letra\n')
                                delay()
                                cleanerScreen()
                                break
                            else:
                                emptyLine()
                                typed.append(word)
                                if word in keyWord:
                                    print(f' A letra {word}, existe na palavra! ')
                                else:
                                    print(f' A letra {word} não existe na palavra! ')
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
                                        archive.close()
                                        archive = open('records.txt', 'r')
                                        contents = archive.read()
                                        archive.close()
                                        archive= open('records.txt', 'a')
                                        print(contents)
                                        quitOrPlay = input(' Deseja jogar novamente ou sair do jogo? ')
                                        cleanerScreen()
                                        if quitGame in quitOrPlay:
                                            quit()
                                else:
                                        print(f'\n A palavra secreta está assim: {temporarySecret}\n')
                                        
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
                                            if quitGame in quitOrPlay:
                                                quit()
                                            cleanerScreen()
                        break
                
    
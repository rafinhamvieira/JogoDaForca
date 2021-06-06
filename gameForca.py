from functionBasic import cleanerScreen, emptyLine, delay

try: #tenta executar o codigo, se não encontrar o arquivo dos registros ele vai para a linha 158
    counterMatches = 1 #contador de partidas para registrar no historico
    while True:
        cleanerScreen()
        #abre o records.txt em modo de leitura
        archive = open('records.txt', 'r')
        #le os arquivos de dentro do registro
        archive.read()
        archive.close()
        #abre os registros em modo de adicionar
        archive= open('records.txt', 'a')        
        while True:
            challengingName = input(' Qual o nome do desafiante? ')
            emptyLine()
            competitorName = input(' Qual o nome do competidor? ') 
            cleanerScreen()  
            keyWord = input(' Qual é a palavra chave? ')
            numberKeyWord = len(keyWord) #verifica quantas letras tem na palavra digitada, se tiver uma letra ou um numero ou nada ele da erro e pede para digitar novamente
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
                archive.write("\n Histórico da partida número: " + str(counterMatches)+ '\n') #registra o histórico das partidas no registro
                archive.write("\n A palavra chave é: " +keyWord)  #registra a palavra chave nos registros
                if keyWord != '': #verifica se a palavra chave está vazia
                    emptyLine()
                    tip1 = input(' Qual a primeira dica? ')
                    emptyLine()
                    tip2 = input(' Qual a segunda dica? ')
                    emptyLine()
                    tip3 = input(' Qual a terceira dica? ')
                    cleanerScreen()
                    
                    archive.write("\n Nome do desafiante: " +challengingName) #registra o nome do competidor e do desafiante no registro
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

                    counter =0 
                    while counter < numberKeyWord:
                        counter += 1
                    asterisksValue = '*' * counter #transforma a palavra chave em asteriscos para se mostrada na tela
                    print(f' A palavra contém {counter} letras\n\n Essa é a palavra: {asterisksValue}\n')
                    temporarySecret = ''
                    while keyWord != temporarySecret: #enquanto a palavra chave ta no temporario secreto
                        choice = input(' Deseja jogar ou pedir uma dica? ')
                        emptyLine()
                        while True:
                            if tip in choice: #se pediu dica irá cair aqui, as dicas serão mostradas apenas uma vez e apos isso elas acabaram
                                if tipCounter1 < 1:
                                    tip in choice
                                    print(' A dica é:', tip1,'\n')
                                    tipCounter1 = 1
                                    choice = play
                                elif tipCounter2 < 1:
                                    tip in choice
                                    emptyLine()
                                    print(' A dica é:',tip2,'\n')
                                    tipCounter2 = 1
                                    choice = play
                                elif tipCounter3 < 1:
                                    tip in choice
                                    emptyLine()
                                    tipCounter3 = 1
                                    print(' A dica é:',tip3,'\n')
                                    choice = play
                                elif tipCounter1 == 1 and tipCounter2 == 1 and tipCounter3 == 1:
                                    emptyLine()
                                    print(' As dicas acabaram!\n ')
                                    choice = play
                            if play in choice:
                                wordList = []
                                word = input(' Qual letra você deseja jogar? ')
                                for element in word:
                                    wordList.append(element) #adiciona a letra jogada na lista das letras
                                while len(wordList) > 1 : #verifica se foi jogada apenas uma letra
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
                                        typed.pop() #tira a letra digitada que não existe na palavra
                                    temporarySecret = '' 
                                    for secretWord in keyWord:
                                        if secretWord in typed:
                                            temporarySecret += secretWord #vai adicionar a letra que existe nos asteriscos
                                        else:
                                            temporarySecret += '*'
                                    if temporarySecret == keyWord: #se a lista estiver igual a palavra chave você venceu
                                            print(f' Parabéns você ganhou, a palavra era {keyWord}')
                                            counterMatches += 1 #adiciona um ao contador de partidas
                                            archive.write("\n Vencedor: " +competitorName) #vai adicionar o vencedor e o perdedor no registro
                                            archive.write("\n Desafiante: " +challengingName+ '\n\n')
                                            archive.close()
                                            archive = open('records.txt', 'r')
                                            contents = archive.read()
                                            archive.close()
                                            archive= open('records.txt', 'a')
                                            print(contents)
                                            quitOrPlay = input(' Deseja jogar novamente ou sair do jogo? ')
                                            cleanerScreen()
                                            if quitGame in quitOrPlay: #sistema para jogar novamente ou sair do jogo
                                                quit()
                                            elif playAgain in quitOrPlay:
                                                break
                                    else:
                                            print(f'\n A palavra secreta está assim: {temporarySecret}\n')
                                    #se a letra não estiver na palavra chave diminue uma chance e se chegar a zero chances voce perdeu
                                    if word not in keyWord:
                                            chances -= 1
                                            print(f' Você ainda tem {chances} chances\n')
                                            emptyLine()
                                            if chances == 0:
                                                print(' Você perdeu! ')
                                                counterMatches += 1
                                                archive.write("\n Vencedor: " +challengingName) #vai adicionar o vencedor e o perdedor no registro
                                                archive.write("\n Competidor: " +competitorName+ '\n\n')
                                                emptyLine()
                                                archive.close()
                                                archive = open('records.txt', 'r')
                                                contents = archive.read()
                                                archive.close()
                                                archive= open('records.txt', 'a')
                                                print(contents)
                                                quitOrPlay = input(' Deseja jogar novamente ou sair do jogo? ')
                                                if quitGame in quitOrPlay: #sistema para jogar novamente ou sair do jogo
                                                    quit()
                                                elif playAgain in quitOrPlay:
                                                    break
                                                cleanerScreen()
                            break
except: #para criar o arquivo de registros caso não exista
    archive = open("records.txt", "w")
    archive.close()
         
    
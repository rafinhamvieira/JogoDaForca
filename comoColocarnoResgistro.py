# w - write
# r - read
# a - append

nomeArquivo = input("Informe o nome do arquivo: ")

try:
    arquivo = open(nomeArquivo, "r")
    conteudo = arquivo.read()
    print(conteudo)
    arquivo.close()
except FileNotFoundError:
    log = open("erros.log", "a")
    log.write("Arquivo nao encontrado :"+nomeArquivo+"\n")
    log.close()
    print("Arquivo não existe!....")


print("terminou o programa.....")
